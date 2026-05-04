# articles/views.py
from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # POST 방식으로 넘어온 데이터를 가져옵니다.
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # DB에 저장
    article = Article(title=title, content=content)
    article.save()
    
    # 저장 후 목록 페이지로 리다이렉트
    return redirect('articles:index')