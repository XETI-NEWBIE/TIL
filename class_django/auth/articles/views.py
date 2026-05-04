from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    # 기존 new, create 함수 공통 코드
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()
    return redirect('articles:index')


def update(request, article_id):
    article = Article.objects.get(pk=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
