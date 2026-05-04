# articles/models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 자동으로 생성 시각 기록
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정될 때마다 시각 갱신
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title