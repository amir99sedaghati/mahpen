from re import L
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login
from django.urls import reverse
from course.models import Season
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from . import permissions
from . import forms
from zarinpal.configurations import CALL_BACK_URL

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
            if self.check_paid_card_status():
                # TODO : send message for change status
                pass
        return response
    
    def check_paid_card_status(self):
        return False

class LoginView(permissions.IsAnnonymous, auth_views.LoginView):
    template_name='user_management/login.html'
    next_page = '/'
    permission_message = 'برای ورود به حساب کاربری دیگر ابتدا باید از حساب کاربری فعلی خارج شوید .'

class ProfielView(CreateView):
    pass

class UserTutorialView(LoginRequiredMixin, TemplateView):
    template_name = 'user_management/tutorials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seasons'] = Season.get_payed_course(request=self.request)
        return context

class UserTutorialView(LoginRequiredMixin, TemplateView):
    template_name = 'user_management/tutorials.html'

    def get_context_data(self, **kwargs):
        from course.models import Season
        context = super().get_context_data(**kwargs)
        context['seasons'] = Season.get_payed_course(request=self.request)
        return context

class UserWalletView(LoginRequiredMixin, TemplateView):
    template_name = 'user_management/wallet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.UserWalletForm()
        return context

    def post(self, request, *arg, **kwargs):
        form = forms.UserWalletForm(request.POST)
        if form.is_valid():
            from zarinpal.views import PayView
            amount = form.cleaned_data['wallet']
            wallet_tr = self.add_wallet_transaction(amount)
            callback_url = CALL_BACK_URL + reverse('callback-wallet' , args=(wallet_tr.id, ))
            return PayView(request=request).send_request(amount, callback_url)
        else:
            form = forms.UserWalletForm()

        return render(request, 'user_management/wallet.html', {'form': form})
    
    def add_wallet_transaction(self, amount):
        from zarinpal.models import WalletTransaction
        return WalletTransaction.objects.create(
            user=self.request.user,
            amount=amount,
        )