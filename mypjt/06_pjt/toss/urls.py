# toss/urls.py
from django.urls import path
from . import views

app_name = 'toss'
urlpatterns = [
    path('', views.index, name='index'),
    # path('save/', views.save, name='save'),
    # 👇 이 줄을 반드시 추가해야 JavaScript의 New EventSource("/run_pipeline/...")가 작동합니다!
    path('run_pipeline/', views.run_crawling_pipeline, name='run_pipeline'),
]