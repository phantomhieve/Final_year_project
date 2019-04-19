from django.urls import path
from . import views as user_views

# add path for users app here
# link to project urls
urlpatterns = [
    path('register/', user_views.register),
    path('', user_views.login),
    path('main/', user_views.main)
]