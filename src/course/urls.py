from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
]


router = DefaultRouter()
router.register(r'card', views.CardViewSet, basename='card')
urlpatterns += router.urls