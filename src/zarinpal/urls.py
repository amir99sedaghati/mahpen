from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
]


router = DefaultRouter()
router.register(r'', views.PayViewSet, basename='pay')
urlpatterns += router.urls