from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CompanySearchForm
from .models import CrawlResult
from .services import (
    augment_comments,
    clean_comments,
    fetch_toss_comments,
    filter_inappropriate_comments,
    summarize_comments,
)


def index(request):
    form = CompanySearchForm(request.POST or None)
    latest_results = CrawlResult.objects.all()[:5]

    if request.method == "POST":
        if not form.is_valid():
            messages.error(request, "회사명을 입력해 주세요.")
            return render(request, "crawler/index.html", {"form": form, "latest_results": latest_results})

        company_name = form.cleaned_data["company_name"]
        try:
            crawl_data = fetch_toss_comments(company_name)
            filtered_comments, filter_message = filter_inappropriate_comments(crawl_data.comments)
            cleaned_comments, iqr_info = clean_comments(filtered_comments)
            augmented_comments, augment_message = augment_comments(cleaned_comments)
            summary = summarize_comments(crawl_data.comments)
            integrated_data = {
                "raw": crawl_data.comments,
                "cleaned": cleaned_comments,
                "augmented": augmented_comments,
            }

            result = CrawlResult.objects.create(
                requested_company=crawl_data.requested_company,
                matched_company=crawl_data.matched_company,
                stock_code=crawl_data.stock_code,
                raw_comments=crawl_data.comments,
                cleaned_comments=cleaned_comments,
                augmented_comments=augmented_comments,
                integrated_data=integrated_data,
                iqr_info=iqr_info,
                summary=summary,
                status_message=f"{filter_message} / {augment_message}",
            )
            messages.success(request, "크롤링과 데이터 처리가 완료되었습니다.")
            return redirect("crawler:result_detail", pk=result.pk)
        except Exception as exc:
            messages.error(request, f"처리 중 문제가 발생했습니다: {exc}")

    return render(request, "crawler/index.html", {"form": form, "latest_results": latest_results})


def result_detail(request, pk):
    result = get_object_or_404(CrawlResult, pk=pk)
    return render(request, "crawler/result_detail.html", {"result": result})
