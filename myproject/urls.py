"""
URL configuration for config_setings_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path, include

from blog.views import BlogListView, BlogCreateView, BlogDeleteView, BlogDetailView, BlogUpdateView
from mail.views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, SettingMailListView, \
    SettingMailCreateView, SettingUpdateView, SettingMailDeleteView, MailingListView, MailingCreateView, \
    MailingUpdateView, MailingDeleteView, LogListView
from users.views import forgotten_password, verification, ProfileView, RegisterView, UserLoginView
from django.contrib.auth.views import LogoutView
from django.views.decorators.cache import cache_page

urlpatterns = [
    # Blog URLs
    path('', BlogListView.as_view(), name='blog'),
    path('create/', cache_page(60)(BlogCreateView.as_view()), name='create_blog'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete_blog'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail_blog'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='edit'),

    # Client URLs
    path('client', ClientListView.as_view(), name='client'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('edit_client/<int:pk>/', ClientUpdateView.as_view(), name='edit_client'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),

    # Setting URLs
    path('list_setting/', SettingMailListView.as_view(), name='list_setting'),
    path('create_setting/', SettingMailCreateView.as_view(), name="create_setting"),
    path('edit_setting/<int:pk>/', SettingUpdateView.as_view(), name='edit_setting'),
    path('delete_setting/<int:pk>/', SettingMailDeleteView.as_view(), name='delete_setting'),

    # Mailing URLs
    path('list_mail/', MailingListView.as_view(), name='list_mail'),
    path('create_mail/', MailingCreateView.as_view(), name="create_mail"),
    path('edit_mail/<int:pk>/', MailingUpdateView.as_view(), name='edit_mail'),
    path('delete_mail/<int:pk>/', MailingDeleteView.as_view(), name='delete_mail'),
    path('mail/', include('mail.urls', namespace='mail')),

    # Log URLs
    path('list_log/', LogListView.as_view(), name='list_log'),

    # User URLs
    path('login/', UserLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verification/', verification, name='verification'),
    path('forgotten_password/', forgotten_password, name='forgotten_password'),
    path('users/', include('users.urls', namespace='users')),
]
