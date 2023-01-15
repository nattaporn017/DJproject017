from django.urls import path
from django.http import  HttpResponse
from ProfileApp import views

urlpatterns = [
    path('info', views.info, name = 'info'),
    path('edu', views.edu, name = 'edu'),
    path('fav', views.fav, name = 'fav'),
    path('prod', views.prod, name = 'prod'),
    path('prod1', views.prod1, name = 'prod1'),
    path('prod2', views.prod2, name = 'prod2'),
    path('prod3', views.prod3, name = 'prod3'),
    path('prod4', views.prod4, name = 'prod4'),
    path('prod5', views.prod5, name = 'prod5'),
    path('prod6', views.prod6, name = 'prod6'),
    path('prod7', views.prod7, name = 'prod7'),
    path('prod8', views.prod8, name = 'prod8'),
    path('idol', views.idol, name = 'idol'),
    # path('head', views.head, name = 'head'),
    # path('menu', views.menu, name = 'menu'),
    # path('base', views.base, name = 'base'),
]