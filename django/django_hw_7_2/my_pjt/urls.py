# my_pjt/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('my_app.urls')), 
]

# [중요] 사용자가 업로드한 미디어 파일을 서빙하기 위한 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)