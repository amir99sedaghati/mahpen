from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='user-sign-up'),
    path('login/', views.LoginView.as_view(), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='user-log-out'),
]