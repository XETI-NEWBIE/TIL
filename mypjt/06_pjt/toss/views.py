# toss/views.py
import os
import json
import ast
import re
import time
import pandas as pd
from django.shortcuts import render
from django.http import StreamingHttpResponse

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 최신 Selenium에서는 webdriver-manager 없이도 동작하지만,
# 문제가 생겼으므로 명시적으로 경로를 잡아주는 방법으로 되돌리거나, 
# 안정적인 버전을 사용합니다. 여기서는 webdriver_manager를 사용합니다.
from webdriver_manager.chrome import ChromeDriverManager
from langchain.chat_models import init_chat_model

from .models import CrawlResult

def index(request):
    return render(request, 'toss/index.html')

def run_llm(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    MODEL = os.getenv("MODEL", "gpt-3.5-turbo") # 기본값 설정
    llm = init_chat_model(MODEL, model_provider="openai", api_key=api_key)
    result = llm.invoke([{"role": "user", "content": prompt}])
    return result.content

def run_crawling_pipeline(request):
    company_name = request.GET.get("company", "삼성전자")
    limit = int(request.GET.get("limit", 20))
    max_scroll = 10

    def event_stream():
        yield f"data: [시작] '{company_name}' 데이터 파이프라인 가동...\n\n"

        # ---------------------------------------------------------
        # 1. Selenium 크롤링
        # ---------------------------------------------------------
        yield f"data: [크롤링] 토스증권 접속 및 회사 검색 중...\n\n"
        
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") # 최신 헤드리스 모드
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # 봇 탐지 우회 옵션 (에러 방지)
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        try:
            # webdriver_manager를 사용하여 자동으로 드라이버 관리
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
        except Exception as e:
             yield f"data: [오류] 크롬 드라이버 실행 실패: {str(e)}\n\n"
             return

        try:
            driver.get("https://www.tossinvest.com/")
            time.sleep(1)

            body = driver.find_element(By.TAG_NAME, "body")
            body.send_keys("/")
            time.sleep(1)

            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='검색어를 입력해주세요']"))
            )
            search_input.send_keys(company_name)
            search_input.send_keys(Keys.ENTER)
            time.sleep(1)

            WebDriverWait(driver, 15).until(EC.url_contains("/order"))
            current_url = driver.current_url
            stock_code = current_url.split("/")[current_url.split("/").index("stocks") + 1]

            community_url = f"https://www.tossinvest.com/stocks/{stock_code}/community"
            driver.get(community_url)
            time.sleep(1)

            try:
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#stock-content"))
                )
            except Exception:
                pass
            time.sleep(2)
            
            yield "data: [크롤링] 페이지 로드 완료, 댓글 수집 중...\n\n"

            comments = []
            last_height = driver.execute_script("return document.body.scrollHeight")
            comment_selectors = [
                "div > div.tc3tm81 > div > div.tc3tm85 > span > span",
                "article.comment span",
                "#stock-content article span",
            ]

            for scroll in range(max_scroll):
                spans = []
                for sel in comment_selectors:
                    spans = driver.find_elements(By.CSS_SELECTOR, sel)
                    if spans:
                        break

                for span in spans:
                    text = span.text.strip()
                    if text and text not in comments:
                        comments.append(text)

                if len(comments) >= limit:
                    break

                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)

                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            comments = comments[:limit]
            original_comments = comments.copy() # 원본 보존
            yield f"data: [크롤링 완료] {len(comments)}개의 댓글 수집 완료.\n\n"
        
        except Exception as e:
            driver.quit()
            yield f"data: [오류] 크롤링 중 문제 발생: {str(e)}\n\n"
            return
            
        driver.quit()

        # ---------------------------------------------------------
        # 2. LLM 부적절 댓글 필터링
        # ---------------------------------------------------------
        if not comments:
            yield "data: [완료] 수집된 데이터가 없습니다.\n\n"
            return

        yield f"data: [부적절 필터] LLM으로 욕설·비방 판별 중...\n\n"
        numbered = "\n".join(f"{i}. {c}" for i, c in enumerate(comments))
        prompt = f"""다음 댓글 목록에서 부적절한 댓글의 번호만 반환해줘. 응답은 반드시 이 형식만: [0, 2, 5] 또는 []\n댓글 목록:\n{numbered}"""
        response = run_llm(prompt).strip()
        
        try:
            to_remove = json.loads(response)
            to_remove_idx = sorted(set(int(x) for x in to_remove if isinstance(x, (int, float)) and 0 <= int(x) < len(comments)))
            for i in reversed(to_remove_idx):
                comments.pop(i)
        except json.JSONDecodeError:
            pass 
            
        yield f"data: [부적절 필터 완료] 남은 댓글 {len(comments)}개\n\n"

        # ---------------------------------------------------------
        # 3. Pandas 전처리
        # ---------------------------------------------------------
        yield "data: [전처리] 특수문자, 반복문자 및 이상치 제거 중...\n\n"
        df = pd.DataFrame(comments, columns=["comment"])
        df = df.dropna(subset=["comment"])
        df["comment"] = df["comment"].astype(str).str.strip()
        df = df[df["comment"] != ""]

        df["clean"] = df["comment"].apply(lambda x: re.sub(r"[^가-힣a-zA-Z0-9\s]", "", x))
        df["clean"] = df["clean"].str.replace(r"\s+", " ", regex=True).str.strip()

        cond_numeric = df["clean"].str.match(r"^\d+$")
        cond_repeat = df["clean"].str.match(r"^[ㅋㅎ]+$")
        cond_english = df["clean"].str.match(r"^[A-Za-z\s]+$")
        cond_none = df["clean"].str.lower() == "none"
        df = df[~(cond_numeric | cond_repeat | cond_english | cond_none)]

        df["length"] = df["clean"].str.len()
        iqr_info = {}
        if len(df) >= 5:
            q1 = df["length"].quantile(0.25)
            q3 = df["length"].quantile(0.75)
            iqr = q3 - q1
            lower = max(5, q1 - 1.5 * iqr)
            upper = q3 + 1.5 * iqr
            df = df[(df["length"] >= lower) & (df["length"] <= upper)]
            iqr_info = {"lower": lower, "upper": upper}
        else:
            df = df[df["length"] >= 3]

        cleaned_result = df["clean"].tolist()
        yield f"data: [전처리 완료] 정제된 데이터 {len(cleaned_result)}개 확보.\n\n"

        # ---------------------------------------------------------
        # 4. LLM 증강
        # ---------------------------------------------------------
        if not cleaned_result:
            yield "data: [증강 스킵] 전처리 후 남은 데이터가 없습니다.\n\n"
            augmented_result = []
        else:
            yield f"data: [데이터 증강] LLM 호출로 문장 의미 확장 중...\n\n"
            prompt = f"{cleaned_result}\n위 리스트의 각각의 문장을, 의미는 유지하면서 다르게 표현해줘. 출력 형식: 대괄호 [ 로 시작해서 대괄호 ] 로 끝나는 파이썬 리스트 형식"
            response = run_llm(prompt)
            
            try:
                augmented_result = ast.literal_eval(str(response).strip())
                if not isinstance(augmented_result, list):
                    augmented_result = []
            except Exception:
                augmented_result = []
                
        yield f"data: [증강 완료] {len(augmented_result)}개의 새로운 데이터 생성.\n\n"

        # ---------------------------------------------------------
        # 5. DB 저장
        # ---------------------------------------------------------
        yield "data: [DB 저장] 결과를 데이터베이스에 저장 중...\n\n"
        CrawlResult.objects.create(
            actual_company_name=company_name,
            original_comments=original_comments,
            cleaned_comments=cleaned_result,
            augmented_comments=augmented_result,
            iqr_threshold=iqr_info
        )

        # ---------------------------------------------------------
        # 6. 완료 및 최종 데이터 전송 (JSON 형태)
        # ---------------------------------------------------------
        final_data = {
            "status": "DONE",
            "company": company_name,
            "original": original_comments,
            "cleaned": cleaned_result,
            "augmented": augmented_result
        }
        yield f"data: {json.dumps(final_data)}\n\n"

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')