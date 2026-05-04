# my_app/models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    # [요구사항] 사용자가 업로드한 파일의 저장 위치를 '/uploaded_files/'로 지정
    # 실제 저장 경로는 MEDIA_ROOT/uploaded_files/ 가 됩니다.
    image = models.ImageField(upload_to='uploaded_files/', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)