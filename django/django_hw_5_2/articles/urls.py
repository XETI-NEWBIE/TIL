from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),       # 전체 목록
    path('new/', views.new, name='new'),       # 글 작성 폼
    path('create/', views.create, name='create'), # 데이터 저장
]