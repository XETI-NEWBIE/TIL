# my_pjt/urls.py

from django.contrib import admin
from django.urls import path
# [요구사항] 미디어 경로 설정을 위해 settings와 static 함수를 import 합니다.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

# [요구사항] url(MEDIA_URL)과 폴더 위치(MEDIA_ROOT)를 인자로 받는 static 함수를 사용합니다.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)