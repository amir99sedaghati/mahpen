from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
]

router = DefaultRouter()
router.register(r'course', views.CourseViewSet, basename='course')
urlpatterns += router.urls