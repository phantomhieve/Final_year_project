from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# add path for users app here
# link to project urls
urlpatterns = [
    path('register/', views.register_view.as_view(),name='register'),
    path('',          views.login_view.as_view(),   name='login'),
    path('check/',    views.check_view.as_view(),   name='check'),
    path('main/', views.main_view),
    path('logout/', views.logout_view, name='logout')
]