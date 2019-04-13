# coding:utf-8
# life is short, you need Python！

from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
