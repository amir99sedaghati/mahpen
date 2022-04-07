from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view()),
]

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'video', views.VideoViewSet, basename='video')
router.register(r'post', views.PostViewSet, basename='post')
urlpatterns += router.urls