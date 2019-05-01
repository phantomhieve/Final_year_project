from django.urls import path, include 
from django.conf.urls import url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('animes/', views.AnimeView.as_view()),
    path('anime/', views.SingleAnimeView.as_view()),
]