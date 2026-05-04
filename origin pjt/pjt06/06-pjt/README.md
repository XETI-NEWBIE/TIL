# 06-pjt 데이터 크롤링 프로젝트

Django 기반 웹 애플리케이션에서 회사명을 입력받아 토스증권 커뮤니티 댓글을 수집하고, 전처리와 LLM 기반 데이터 증강 및 요약을 수행하는 프로젝트입니다.

## 구현 기능

- 회사명 입력 및 빈 값 검증
- 토스증권 회사 검색 후 최상단 종목 자동 선택
- 선택 종목 커뮤니티 댓글 20개 수집
- 결측치, 특수문자, 반복 패턴, 길이 이상치 전처리
- LLM API를 활용한 부적절 댓글 필터링
- LLM API를 활용한 댓글 데이터 증강
- 원본 댓글, 정제 댓글, 증강 댓글 통합 출력
- 댓글 요약 생성
- 처리 결과 DB 저장
- 검색 결과 및 댓글 미존재 예외 안내

## 실행 방법

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

브라우저에서 `http://127.0.0.1:8000/`로 접속합니다.

## 환경 변수

프로젝트 루트에 `.env` 파일을 만들고 다음 값을 설정합니다.

```env
model="gpt-5-nano"
OPENAI_API_KEY="YOUR_API_KEY"
```

## 학습 내용

- Django의 MTV 구조와 URL, View, Template 연결 흐름
- Selenium을 활용한 동적 웹 페이지 데이터 수집
- pandas와 정규 표현식을 활용한 텍스트 전처리
- LLM API 호출 결과를 웹 서비스 데이터 처리 흐름에 통합하는 방법
- JSONField를 활용한 단계별 데이터 저장

## 느낀 점

크롤링 대상 페이지는 구조가 바뀔 수 있어 선택자를 여러 개 준비하고 예외 상황을 안내하는 흐름이 중요했습니다. 또한 LLM 처리는 API 키, 응답 형식, 실패 가능성을 함께 고려해야 실제 서비스 흐름에서 안정적으로 사용할 수 있음을 배웠습니다.
