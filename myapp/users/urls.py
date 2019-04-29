from django.urls import path
from . import views as user_views

# add path for users app here
# link to project urls
urlpatterns = [
    path('register/', user_views.register_view),
    path('', user_views.login_view),
    path('main/', user_views.main_view)
]