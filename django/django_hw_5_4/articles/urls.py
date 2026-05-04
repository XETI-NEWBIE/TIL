from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # 상세 조회 경로: /articles/<pk>/
    path('<int:article_pk>/', views.detail, name='detail'),
    # 삭제 경로: /articles/<pk>/delete/
    path('<int:article_pk>/delete/', views.delete, name='delete'),
]