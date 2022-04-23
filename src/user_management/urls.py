from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='user-sign-up'),
    path('login/', views.LoginView.as_view(), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='user-log-out'),
    path('profile/', views.ProfielView.as_view(), name='user-profile'),
    path('tutorials/', views.UserTutorialView.as_view(), name='user-tutorials'),
    path('wallet/', views.UserWalletView.as_view(), name='user-wallet'),
]