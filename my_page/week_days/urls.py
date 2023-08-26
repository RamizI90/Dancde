from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<int:days>/', views.get_info_about_days_by_number),
    path('<str:days>/', views.get_info_about_days, name='week_name'),

]
