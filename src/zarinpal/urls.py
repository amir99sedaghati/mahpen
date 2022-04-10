from . import views
from django.urls import path

urlpatterns = [
    path('card/<int:pk>/pay/', views.PayView.as_view(), 'card-pay'),
    path('card/<int:pk>/callback/', views.CallBackView.as_view(), 'callback-pay')
]