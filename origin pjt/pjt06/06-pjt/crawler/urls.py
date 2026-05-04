from django.urls import path

from . import views


app_name = "crawler"

urlpatterns = [
    path("", views.index, name="index"),
    path("results/<int:pk>/", views.result_detail, name="result_detail"),
]
