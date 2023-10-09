from .import views
from blog.apps import BlogConfig
from django.urls import path
from blog.views import (
    BlogListView,
    BlogCreateView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = BlogConfig.name


urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('users_home/', views.users_home, name='users_home'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]