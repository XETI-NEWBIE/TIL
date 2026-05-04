










# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# 요구사항: django의 기본 User 모델을 상속받고, 추가 필드는 정의하지 않음
class User(AbstractUser):
    pass
