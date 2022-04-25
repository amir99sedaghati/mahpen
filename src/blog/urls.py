from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('video/<int:pk>/', views.VideoDetailView.as_view(), name='video-detail'),
    path('video/', views.VideoListView.as_view(), name='video-list'),
]
