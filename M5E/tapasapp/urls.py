from django.urls import path
from . import views


urlpatterns = [
    path('basic_list', views.view_basic_list, name='view_basic_list'),
    path('', views.view_menu, name='view_menu'),
    path('add_menu', views.add_menu, name='add_menu'),
]