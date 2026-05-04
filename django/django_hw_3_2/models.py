# articles/models.py

from django.db import models

class Article(models.Model):
    # varchar(15) -> 최대 길이가 15인 문자열 필드
    title = models.CharField(max_length=15)
    
    # TEXT -> 길이 제한이 없는 텍스트 필드
    content = models.TextField()

    # (선택사항) admin 사이트나 쉘에서 객체를 확인할 때 제목이 보이도록 설정
    def __str__(self):
        return self.title