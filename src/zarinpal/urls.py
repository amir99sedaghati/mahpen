from . import views
from django.urls import path

urlpatterns = [
    path('<int:pk>/pay/', views.PayView.as_view(), name='card-pay'),
    path('<int:pk>/callback/<int:amount>/', views.CallBackView.as_view(), name='callback-pay')
]