from . import views
from django.urls import path

urlpatterns = [
    path('<int:pk>/pay/', views.PayView.as_view(), name='card-pay'),
    path('<int:pk>/callback/<int:amount>/', views.CallBackView.as_view(), name='callback-pay'),
    path('<int:pk>/wallet-callback/', views.CallBackWallet.as_view(), name='callback-wallet'),
    path('<int:pk>/pay/wallet/', views.PayByWallet.as_view(), name='wallet-pay'),
]