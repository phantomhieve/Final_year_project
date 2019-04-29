from django.urls import path
from . import views as user_views

# add path for users app here
# link to project urls
urlpatterns = [
    path('register/', user_views.register_view, name='register'),
    path('', user_views.login_view, name='login'),
    path('main/', user_views.main_view),
    path('logout/', user_views.logout_view, name='logout')
]