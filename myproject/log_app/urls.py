from django.urls import path
from .views import MailingLogListView, MailingLogDetailView, MailingLogCreateView, MailingLogUpdateView, MailingLogDeleteView

urlpatterns = [
    path('list/', MailingLogListView.as_view(), name='mailinglog-list'),
    path('detail/<int:pk>/', MailingLogDetailView.as_view(), name='mailinglog-detail'),
    path('create/', MailingLogCreateView.as_view(), name='mailinglog-create'),
    path('update/<int:pk>/', MailingLogUpdateView.as_view(), name='mailinglog-update'),
    path('delete/<int:pk>/', MailingLogDeleteView.as_view(), name='mailinglog-delete'),
]
