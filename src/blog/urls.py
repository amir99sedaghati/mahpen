from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view()),
]

router = DefaultRouter()
router.register(r'blog/category', views.CategoryViewSet, basename='category')
router.register(r'blog/video', views.VideoViewSet, basename='video')
router.register(r'blog/post', views.PostViewSet, basename='post')
urlpatterns += router.urls