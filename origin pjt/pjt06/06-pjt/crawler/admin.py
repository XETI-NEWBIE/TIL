from django.contrib import admin

from .models import CrawlResult


@admin.register(CrawlResult)
class CrawlResultAdmin(admin.ModelAdmin):
    list_display = ("matched_company", "requested_company", "stock_code", "created_at")
    search_fields = ("matched_company", "requested_company", "stock_code")
    readonly_fields = ("created_at",)
