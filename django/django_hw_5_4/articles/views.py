from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

# 1. 메인 페이지 (전체 목록)
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

# 2. 상세 조회 페이지 (요구사항 구현)
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# 3. 글쓰기 페이지 로딩
def new(request):
    return render(request, 'articles/new.html')

# 4. 글 생성 로직 (DB 저장)
def create(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:index')
    return redirect('articles:new')

# 5. 글 삭제 로직 (POST 요청만 허용 - 요구사항 구현)
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)