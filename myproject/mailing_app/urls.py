from django.urls import path
from .views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView

urlpatterns = [
    path('list/', MailingListView.as_view(), name='mailing-list'),
    path('detail/<int:pk>/', MailingDetailView.as_view(), name='mailing-detail'),
    path('create/', MailingCreateView.as_view(), name='mailing-create'),
    path('update/<int:pk>/', MailingUpdateView.as_view(), name='mailing-update'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing-delete'),
]
