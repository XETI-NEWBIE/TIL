import ast
import json
import os
import re
import time
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from django.conf import settings
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


BASE_DIR = Path(settings.BASE_DIR)
CHROME_DRIVER_PATH = BASE_DIR / "chromedriver-win64" / "chromedriver.exe"
COMMENT_LIMIT = 20

load_dotenv(BASE_DIR / ".env")


@dataclass
class TossCrawlData:
    requested_company: str
    matched_company: str
    stock_code: str
    comments: list[str]


def make_driver() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation", "enable-logging"],
    )
    service = Service(executable_path=str(CHROME_DRIVER_PATH), log_output=os.devnull)
    return webdriver.Chrome(service=service, options=options)


def fetch_toss_comments(company_name: str, limit: int = COMMENT_LIMIT) -> TossCrawlData:
    if not company_name.strip():
        raise ValueError("회사명을 입력해 주세요.")

    print(f"[F103] 회사 검색 시작: {company_name}", flush=True)
    driver = make_driver()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.tossinvest.com/")
        print("[F103] 토스증권 접속 완료", flush=True)
        body = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        body.send_keys("/")

        search_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='검색어를 입력해주세요']")
            )
        )
        search_input.clear()
        search_input.send_keys(company_name)
        search_input.send_keys(Keys.ENTER)

        wait.until(EC.url_contains("/order"))
        stock_code = extract_stock_code(driver.current_url)
        print(f"[F103] 종목 코드 확인: {stock_code}", flush=True)
        driver.get(f"https://www.tossinvest.com/stocks/{stock_code}/community")

        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#stock-content")))
        except TimeoutException:
            pass

        time.sleep(2)
        matched_company = find_company_name(driver, company_name)
        print(f"[F104] 커뮤니티 댓글 수집 시작: {matched_company}", flush=True)
        comments = collect_comments(driver, limit)
        if not comments:
            raise ValueError("댓글 데이터를 찾지 못했습니다.")
        print(f"[F104] 댓글 {len(comments)}개 수집 완료", flush=True)

        return TossCrawlData(company_name, matched_company, stock_code, comments)
    finally:
        driver.quit()


def extract_stock_code(url: str) -> str:
    parts = url.split("/")
    if "stocks" not in parts:
        raise ValueError("검색 결과에서 종목 상세 페이지로 이동하지 못했습니다.")
    return parts[parts.index("stocks") + 1]


def find_company_name(driver: webdriver.Chrome, fallback: str) -> str:
    for selector in ("h1", "[data-testid='stock-name']", "#stock-content h1", "main h1"):
        for element in driver.find_elements(By.CSS_SELECTOR, selector):
            text = element.text.strip()
            if text:
                return text.splitlines()[0]
    return fallback


def collect_comments(driver: webdriver.Chrome, limit: int) -> list[str]:
    comments: list[str] = []
    last_height = driver.execute_script("return document.body.scrollHeight")
    selectors = [
        "div > div.tc3tm81 > div > div.tc3tm85 > span > span",
        "article.comment span",
        "#stock-content article span",
        "#stock-content span",
    ]

    for _ in range(12):
        for selector in selectors:
            for span in driver.find_elements(By.CSS_SELECTOR, selector):
                text = span.text.strip()
                if is_probable_comment(text) and text not in comments:
                    comments.append(text)
                    if len(comments) >= limit:
                        return comments[:limit]
            if comments:
                break

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    return comments[:limit]


def is_probable_comment(text: str) -> bool:
    if len(text) < 2:
        return False
    ignored = {"커뮤니티", "뉴스", "주문", "차트", "토론", "인기", "최신", "더 보기"}
    return text not in ignored


def run_llm(prompt: str) -> str:
    load_dotenv(BASE_DIR / ".env", override=True)

    api_key = os.getenv("OPENAI_API_KEY", "").strip().strip('"')
    model = (
        os.getenv("MODEL")
        or os.getenv("model")
        or os.getenv("OPENAI_MODEL")
        or "gpt-5-nano"
    ).strip().strip('"')

    if not api_key:
        raise RuntimeError(".env에 OPENAI_API_KEY가 없습니다.")

    llm = init_chat_model(model, model_provider="openai", api_key=api_key)
    response = llm.invoke([{"role": "user", "content": prompt}])
    return response.content.strip()


def parse_list(text: str) -> list:
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        value = ast.literal_eval(text)
    return value if isinstance(value, list) else []


def filter_inappropriate_comments(comments: list[str]) -> tuple[list[str], str]:
    print("[F105] 부적절 댓글 필터 시작", flush=True)
    numbered = "\n".join(f"{idx}. {comment}" for idx, comment in enumerate(comments))
    prompt = f"""
다음 댓글 목록에서 부적절한 댓글(욕설, 혐오, 비방, 선정성, 과도한 비난 등)의 번호만 JSON 배열로 알려줘.
번호는 0부터 시작하고 응답은 반드시 [0, 2] 또는 [] 같은 JSON 배열만 작성해.

댓글 목록:
{numbered}
"""
    try:
        indexes = parse_list(run_llm(prompt))
    except Exception as exc:
        return comments[:], f"부적절 댓글 LLM 필터 생략: {exc}"

    remove_indexes = {
        int(idx)
        for idx in indexes
        if isinstance(idx, (int, float)) and 0 <= int(idx) < len(comments)
    }
    filtered = [comment for idx, comment in enumerate(comments) if idx not in remove_indexes]
    return filtered, f"부적절 댓글 {len(remove_indexes)}개 제거"


def clean_comments(comments: list[str]) -> tuple[list[str], dict]:
    print("[F105] 댓글 전처리 시작", flush=True)
    df = pd.DataFrame(comments, columns=["comment"])
    df = df.dropna(subset=["comment"])
    df["comment"] = df["comment"].astype(str).str.strip()
    df = df[df["comment"] != ""]

    df["clean"] = df["comment"].apply(lambda value: re.sub(r"[^가-힣a-zA-Z0-9\s]", "", value))
    df["clean"] = df["clean"].str.replace(r"\s+", " ", regex=True).str.strip()

    useless = (
        df["clean"].str.match(r"^\d+$")
        | df["clean"].str.match(r"^[ㅋㅎㅠㅜ]+$")
        | df["clean"].str.match(r"^[A-Za-z\s]+$")
        | (df["clean"].str.lower() == "none")
    )
    df = df[~useless]
    df["length"] = df["clean"].str.len()

    iqr_info = {
        "q1": None,
        "q3": None,
        "iqr": None,
        "lower": 3,
        "upper": None,
        "before_count": len(comments),
    }

    if len(df) >= 5:
        q1 = float(df["length"].quantile(0.25))
        q3 = float(df["length"].quantile(0.75))
        iqr = q3 - q1
        lower = max(3, q1 - 1.5 * iqr)
        upper = q3 + 1.5 * iqr
        df = df[(df["length"] >= lower) & (df["length"] <= upper)]
        iqr_info.update({"q1": q1, "q3": q3, "iqr": iqr, "lower": lower, "upper": upper})
    else:
        df = df[df["length"] >= 3]

    cleaned = df["clean"].drop_duplicates().tolist()
    iqr_info["after_count"] = len(cleaned)
    return cleaned, iqr_info


def augment_comments(comments: list[str]) -> tuple[list[str], str]:
    print("[F106] 댓글 증강 시작", flush=True)
    if not comments:
        return [], "증강할 정제 댓글이 없습니다."

    prompt = f"""
아래 댓글 목록의 의미는 유지하되 자연스러운 한국어 문장으로 다르게 표현한 증강 데이터를 만들어줘.
응답은 반드시 JSON 리스트만 작성해.

댓글 목록:
{json.dumps(comments, ensure_ascii=False)}
"""
    try:
        augmented = parse_list(run_llm(prompt))
    except Exception as exc:
        return [], f"데이터 증강 생략: {exc}"

    return [str(item).strip() for item in augmented if str(item).strip()], "증강 데이터 생성 완료"


def summarize_comments(comments: list[str]) -> str:
    print("[F110] 댓글 요약 시작", flush=True)
    if not comments:
        return ""

    prompt = f"""
다음 주식 커뮤니티 댓글의 핵심 분위기와 주요 의견을 3문장 이내로 요약해줘.

댓글 목록:
{json.dumps(comments, ensure_ascii=False)}
"""
    try:
        return run_llm(prompt)
    except Exception as exc:
        return f"요약 생성 생략: {exc}"
