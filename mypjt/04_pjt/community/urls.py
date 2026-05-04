from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    # F401: 자산 목록 
    path('', views.index, name='index'),
    # F403: 자산별 게시판
    path('<str:asset_id>/', views.board, name='board'),
    # F404: 게시글 생성
    path('<str:asset_id>/create/', views.create, name='create'),
    # F405: 게시글 상세 조회
    path('<str:asset_id>/<int:post_id>/', views.detail, name='detail'),
    # F406: 게시글 수정
    path('<str:asset_id>/<int:post_id>/update/', views.update, name='update'),
    # F407: 게시글 삭제
    path('<str:asset_id>/<int:post_id>/delete/', views.delete, name='delete'),
]