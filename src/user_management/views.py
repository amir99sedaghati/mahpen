from re import L
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from . import permissions
from . import forms

class SignUpView(permissions.IsAnnonymous, CreateView):
    success_url = '/'
    login_url = '/'
    model = get_user_model()
    template_name = 'user_management/sign_up.html'
    form_class = forms.UserSignUpForm
    permission_message = 'برای ثبت نام کاربر جدید باید از حساب کاربری فعلی خارج شوید . '
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(username=self.object.username, password=self.object.password)
        if user is not None :
            login(self.request, user)
        return response

class LoginView(permissions.IsAnnonymous, auth_views.LoginView):
    template_name='user_management/login.html'
    next_page = '/'
    permission_message = 'برای ورود به حساب کاربری دیگر ابتدا باید از حساب کاربری فعلی خارج شوید .'

