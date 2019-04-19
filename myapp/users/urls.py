from django.urls import path
from . import views as user_views

# add path for users app here
# link to project urls
urlpatterns = [
    path('', user_views.register)
]