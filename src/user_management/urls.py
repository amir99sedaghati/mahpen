from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
]

router = DefaultRouter()
router.register(r'', views.UserViewSet, basename='user')
urlpatterns += router.urls