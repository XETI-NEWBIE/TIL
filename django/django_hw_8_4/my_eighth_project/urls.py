from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # accounts/ 로 들어오는 모든 요청을 accounts 앱으로 보냅니다.
    path('accounts/', include('accounts.urls')), 
]