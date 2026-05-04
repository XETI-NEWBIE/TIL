from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # nickname: 문자열, 필수 입력
    nickname = models.CharField(max_length=50)
    # interest_stocks: 여러 종목을 쉼표로 구분하여 저장, 빈 값 허용
    interest_stocks = models.CharField(max_length=255, blank=True)
    # profile_image: 프로필 이미지, blank/null 허용
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)