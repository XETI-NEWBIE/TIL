# articles/admin.py

from django.contrib import admin
# 현재 폴더의 models.py에서 Article 모델을 가져옵니다.
from .models import Article

# 관리자 페이지에 Article 모델을 등록합니다.
admin.site.register(Article)