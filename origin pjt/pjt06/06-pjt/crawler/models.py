from django.db import models


class CrawlResult(models.Model):
    requested_company = models.CharField("입력 회사명", max_length=100)
    matched_company = models.CharField("실제 종목명", max_length=100)
    stock_code = models.CharField("종목 코드", max_length=30)
    raw_comments = models.JSONField("원본 댓글 목록", default=list)
    cleaned_comments = models.JSONField("정제 댓글 목록", default=list)
    augmented_comments = models.JSONField("증강 댓글 목록", default=list)
    integrated_data = models.JSONField("통합 결과", default=dict)
    iqr_info = models.JSONField("IQR 임계값 정보", default=dict)
    summary = models.TextField("댓글 요약", blank=True)
    status_message = models.TextField("처리 메시지", blank=True)
    created_at = models.DateTimeField("생성 일시", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.matched_company} - {self.created_at:%Y-%m-%d %H:%M}"
