from django.contrib.auth.views import LogoutView
from users.apps import UserConfig
from django.urls import path
from users.views import RegisterView, ProfileView, verification, forgotten_password, UserLoginView

app_name = UserConfig.name


urlpatterns = [
    path('', UserLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verification/', verification),
    path('forgotten_password/', forgotten_password, name='forgotten_password')
]