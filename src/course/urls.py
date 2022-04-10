from . import views
from django.urls import path

urlpatterns = [
    path('', views.CardView.as_view(), name='card-detail'),
]

