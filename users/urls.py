from django.contrib.auth.views import LogoutView

from blog import views
from users.apps import UserConfig
from django.urls import path

from users.views import (
    RegisterView,
    ProfileView,
    verification,
    forgotten_password,
    UserLoginView
)
app_name = UserConfig.name


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verification/', verification, name='verification'),
    path('forgotten_password/', forgotten_password, name='forgotten_password'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]