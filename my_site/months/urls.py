from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('seasons/', views.index_season),
    path('seasons/<str:season>/', views.get_season, name='season_name'),
    path('<int:month>/', views.get_info_month_by_number),
    path('<str:month>/', views.get_info_month, name='month_name'),
]
