# -*-coding:utf-8-*-
from django.urls import path

from Two import views

urlpatterns = [
    path('getuser/', views.get_user),
    path('getusers/', views.get_users),
]