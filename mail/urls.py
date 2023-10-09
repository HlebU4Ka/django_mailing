from mail.apps import MailConfig
from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import RegisterView, verification, forgotten_password, UserLoginView, ProfileView
from . import views
from .views import (
    ClientCreateView,
    ClientListView,
    ClientUpdateView,
    ClientDeleteView,
    SettingMailListView,
    SettingMailCreateView,
    SettingUpdateView,
    SettingMailDeleteView,
    MailingListView,
    MailingCreateView,
    MailingUpdateView,
    MailingDeleteView,
    LogListView,
    title,
)

app_name = MailConfig.name

urlpatterns = [
    path('client/', views.ClientListView.as_view(), name='client'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('settings/', SettingMailListView.as_view(), name='list_setting'),
    path('settings/create/', SettingMailCreateView.as_view(), name='create_setting'),
    path('settings/<int:pk>/update/', SettingUpdateView.as_view(), name='update_setting'),
    path('settings/<int:pk>/delete/', SettingMailDeleteView.as_view(), name='delete_setting'),

    path('mail/', MailingListView.as_view(), name='list_mail'),
    path('mail/create/', MailingCreateView.as_view(), name='create_mail'),
    path('mail/<int:pk>/update/', MailingUpdateView.as_view(), name='update_mail'),
    path('mail/<int:pk>/delete/', MailingDeleteView.as_view(), name='delete_mail'),

    path('log/', LogListView.as_view(), name='log_list'),
    path('', title, name='home'),
]
