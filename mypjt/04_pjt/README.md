# 📊 04_pjt: 금융 자산 정보 토론 게시판 (Findive Community)

## 🎯 프로젝트 목표
- Django의 MVT(Model-View-Template) 디자인 패턴을 이해하고 전반적인 웹 서비스 흐름을 구축한다.
- 로컬 JSON 파일(`assets.json`) 데이터를 파싱하여 화면에 동적으로 렌더링한다.
- Django ORM을 활용하여 금융 자산별 게시판 구조를 설계하고, 게시글 CRUD(Create, Read, Update, Delete) 로직을 완벽하게 구현한다.
- 존재하지 않는 경로 및 ID 접근 등 예외 상황 발생 시, 사용자 친화적인 Custom 404 에러 페이지를 제공하여 UX를 개선한다.

<br>

## 🛠 기술 스택
- **Language**: Python 3.x
- **Framework**: Django 5.x
- **Database**: SQLite3
- **Frontend**: HTML5, CSS (자체 UI/UX 스타일링 - Findive 테마 적용)
- **Version Control**: Git, GitLab

<br>

## 🚀 상세 구현 기능 및 로직 설명

| 번호 | 분류 | 요구사항명 | 구현 내용 상세 |
|:---:|:---|:---|:---|
| F401 | 자산 데이터 | 자산 목록 출력 | `os`와 `json` 라이브러리를 활용해 `BASE_DIR` 하위의 `assets.json`을 읽어오는 공통 헬퍼 함수를 구현. 딕셔너리 리스트를 템플릿으로 넘겨 반복문(`{% for %}`)으로 렌더링. |
| F402 | 모델 설계 | 게시판 모델 작성 | `models.Model`을 상속받아 `Post` 모델 정의. `asset_id`(CharField), `title`, `content`(TextField), `created_at`(DateTimeField, auto_now_add) 등 데이터베이스 스키마 구축 및 마이그레이션 완료. |
| F403 | 게시판 화면 | 자산별 게시판 구현 | URL의 Path Converter(`<str:asset_id>`)를 뷰 함수 인자로 받아, `Post.objects.filter(asset_id=asset_id)`를 통해 특정 자산의 게시글만 쿼리셋으로 추출 후 최신순(`-created_at`) 정렬. |
| F404 | 게시글 관리 | 게시글 생성 | `forms.ModelForm`을 활용해 안전한 입력 폼 구성. `request.method == 'POST'`일 때 폼 유효성 검사(`is_valid()`) 후, `commit=False`로 객체를 임시 저장하여 URL 파라미터의 `asset_id`를 주입한 뒤 최종 DB 저장. |
| F405 | 게시글 관리 | 상세 조회 | `get_object_or_404(Post, pk=post_id)`를 사용하여 게시글 데이터를 가져오고, 템플릿의 `{{ post.content|linebreaks }}` 필터를 통해 본문의 줄바꿈을 유지하며 출력. |
| F406 | 게시글 관리 | 게시글 수정 | `instance=post` 옵션을 사용해 기존 게시글 데이터를 폼에 바인딩하여 렌더링. 수정 후 `save()` 시 기존 레코드가 업데이트(UPDATE 쿼리)되도록 구현. |
| F407 | 게시글 관리 | 게시글 삭제 | 보안을 위해 삭제 요청은 반드시 `POST` 메서드로만 동작하도록 제한. `post.delete()` 실행 후 자산별 게시판 목록(`community:board`)으로 `redirect` 처리. |
| F408 | 예외 처리 | Custom 404 페이지 | 없는 자산 ID 접근 시 `render(..., status=404)`를 반환하도록 `views.py` 분기 처리. 존재하지 않는 게시글은 `get_object_or_404`가 발생시키는 예외를 활용해 잘못된 접근 차단. |

<br>

## 🧠 구체적인 학습 내용

**1. Django MVT 패턴의 데이터 흐름 이해**
파이썬 언어 자체의 로직 구성에 집중하다가, 처음으로 프레임워크를 통해 화면과 데이터를 연결해 보았습니다. 
- **URL Dispatcher:** `urls.py`에서 요청된 URL을 분석하여 알맞은 뷰로 연결하는 과정.
- **View & Model:** `views.py`에서 DB(Model)에 ORM으로 쿼리를 날려 데이터를 가져오거나 가공하는 과정.
- **Template:** 파이썬의 딕셔너리(Context) 형태 데이터를 HTML 파일로 넘겨 `Django Template Language (DTL)`로 동적 화면을 구성하는 전체 사이클을 명확히 이해했습니다.

**2. Path Converter와 404 에러 처리 메커니즘**
게시글 상세 조회(`/<str:asset_id>/<int:post_id>/`) 테스트 중, 정수형(`int`)이 들어와야 할 자리에 문자열이 들어오면 장고가 아예 해당 URL 패턴을 매칭하지 못해 뷰 로직에 도달하기도 전에 에러가 난다는 사실을 배웠습니다. 이를 통해 프레임워크가 라우팅 단계에서부터 어떻게 데이터를 필터링하고 예외를 던지는지 알게 되었고, 디버그 모드(`DEBUG=True`)의 동작 방식을 이해했습니다.

**3. 가상환경(venv) 및 디렉토리 구조 관리의 중요성**
개발 컴퓨터를 변경하고 프로젝트를 세팅하는 과정에서 가상환경 복원과 디렉토리 경로 문제(`manage.py` not found)를 겪었습니다.
가상환경 디렉토리는 로컬 환경에 종속되므로 Git으로 추적하지 않고 `.gitignore`에 등록해야 한다는 점을 체감했으며, `requirements.txt` 또는 `pip install`을 통해 새로운 환경에서 의존성을 재구축하는 프로세스를 익혔습니다.

<br>

## 💦 느낀 점 및 회고

단순히 터미널에 텍스트를 출력하던 파이썬 실습을 넘어, 실제 동작하는 웹 서비스(Findive)의 형태를 갖춘 결과물을 보며 큰 성취감을 느꼈습니다. 특히 `ModelForm`을 활용해 반복적인 폼 생성 작업을 줄이면서도, CSS를 결합해 깔끔하고 퀄리티 있는 UI를 만들어내는 과정이 흥미로웠습니다.

과정 중에 경로 설정 오류나 URL 매칭 오류 등 여러 난관이 있었지만, 터미널의 에러 로그를 꼼꼼히 읽고 장고의 동작 원리(어느 단계에서 튕겨냈는가?)를 역추적하며 해결할 수 있었습니다. 이번 관통 프로젝트를 통해 단순히 코드를 따라 치는 것을 넘어, '프레임워크가 데이터를 어떻게 주고받는지' 그 맥락을 짚어내는 시야를 기를 수 있어 매우 유익했습니다.

<br>

## 🧑‍💻 팀원 정보
* **이름:** 홍채원
* **역할:** 모델링, CRUD 뷰 로직 설계, URL 라우팅, 프론트엔드 UI/UX 커스텀(HTML/CSS), 에러 트러블슈팅