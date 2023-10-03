from django.urls import path
from .views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

urlpatterns = [
    path('list/', ClientListView.as_view(), name='client-list'),
    path('detail/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('create/', ClientCreateView.as_view(), name='client-create'),
    path('update/<int:pk>/', ClientUpdateView.as_view(), name='client-update'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='client-delete'),
]
