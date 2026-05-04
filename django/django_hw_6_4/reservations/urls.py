from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.index, name='index'),
    # new 경로는 삭제하고 create만 남깁니다!
    path('create/', views.create, name='create'),
]