# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# 커스텀 User 모델과 기본 UserAdmin 설정을 연결하여 관리자 페이지에 등록
admin.site.register(User, UserAdmin)