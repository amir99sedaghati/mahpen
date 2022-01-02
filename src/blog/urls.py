from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = []

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet, basename='category')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'post', views.PostViewSet, basename='post')
urlpatterns += router.urls