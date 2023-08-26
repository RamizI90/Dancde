
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('posts/', views.posts),
    path('posts/<int:number_post>', views.get_number_post),
    path('posts/<name_post>', views.get_info_post),
]
