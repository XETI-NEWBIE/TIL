from django.db import models

class CrawlResult(models.Model):
    # 실제 매칭된 종목의 공식 명칭[cite: 29]
    actual_company_name = models.CharField(max_length=100)
    
    # 원본 댓글 목록[cite: 29]
    original_comments = models.JSONField(default=list)
    
    # 정제 댓글 목록[cite: 29]
    cleaned_comments = models.JSONField(default=list)
    
    # 증강 댓글 목록[cite: 29]
    augmented_comments = models.JSONField(default=list)
    
    # IQR 임계값 정보[cite: 29]
    iqr_threshold = models.JSONField(null=True, blank=True)
    
    # 생성 일시[cite: 29]
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.actual_company_name} - {self.created_at}"