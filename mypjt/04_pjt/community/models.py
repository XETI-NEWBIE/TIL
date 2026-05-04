from django.db import models

class Post(models.Model):
    asset_id = models.CharField(max_length=50) # 금융 자산 ID 
    title = models.CharField(max_length=200)   # 게시글 제목 
    content = models.TextField()               # 게시글 내용 
    author = models.CharField(max_length=50, default="익명") # 작성자 
    created_at = models.DateTimeField(auto_now_add=True)     # 생성 일자 
    updated_at = models.DateTimeField(auto_now=True)         # 수정 일자 

    def __str__(self):
        return self.title