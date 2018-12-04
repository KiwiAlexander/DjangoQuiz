from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/home/', views.index, name='index'),
    path('dataView/', views.dataView, name='dataView'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('game/', views.game, name='game'),
    path('createquiz/', views.createquiz, name='createquiz'),
    path('playgame/<int:pk>/', views.playgame, name='playgame'),
    path('playgame/<int:pk>/<int:qnum>', views.playgame, name='playgame'),
    path('scoreboard/', views.scoreboard, name='scoreboard'),
]