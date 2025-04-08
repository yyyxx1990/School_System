# -*-coding:utf-8-*-
from django.conf.urls import url
from django.urls import path

from App import views

urlpatterns = [
    path('addpersons/', views.add_persons),
    path('getpersons/', views.get_persons),
    path('addperson/', views.add_person),
    path('getperson/', views.get_person),
]
