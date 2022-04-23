from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from suds.client import Client
from .models import Pay
from django.shortcuts import get_object_or_404
from course.models import Card
from django.views.generic.base import View
from user_management import handlers
from django.shortcuts import render
from .configurations import *
from user_management.permissions import IsAuthenticated

class PayView(IsAuthenticated, View):
    permission_message = 'برای پرداخت ابتدا باید حساب کاربری خودتان شوید .'

    def card_queryset(self):
        return Card.objects.filter(user=self.request.user)

    def post(self, request, pk, *arg, **kwargs):
        card = get_object_or_404(self.card_queryset().exclude(status=Card.PAID) , pk=pk)
        card.change_status(Card.FREEZE)
        amount = card.calculate_amount()
        call_back_url = CALL_BACK_URL + reverse('callback-pay' , args=(card.id, amount, ))
        return self.send_request(amount, call_back_url)

    def send_request(self, amount, call_back_url):
        client = Client(ZARINPAL_WEBSERVICE)
        result = client.service.PaymentRequest(
            MMERCHANT_ID,
            amount,
            DESCRIPTION,
            self.request.user.email,
            None,
            call_back_url,
        )
        if result.Status == 100:
            return redirect(START_PAY + result.Authority)
        else:
            return handlers.Handler.as_view()

class CallBackView(View):
    def card_queryset(self):
        return Card.objects.filter(user=self.request.user)
    
    def get(self, request, pk, amount):
        card = get_object_or_404(self.card_queryset().filter(status=Card.FREEZE) , pk=pk)
        if request.GET.get('Status') == 'OK':
            amount = int(float(amount))
            client = Client(ZARINPAL_WEBSERVICE)
            
            result = client.service.PaymentVerification(
                MMERCHANT_ID,
                request.GET.get('Authority'),
                amount,
            )
            
            Pay.objects.create(
                card = card ,
                amount = amount ,
                email = request.GET.get('email') ,
                status = result.Status ,
                authority = request.GET.get('Authority') ,
            )

            if result.Status == 100 or result.Status == 101:
                card.change_status(Card.PAID)
                template_name = 'success.html'
            else:
                card.change_status(Card.INPROCESS)
                messages.warning(self.request, 'پرداخت موفقیت آمیز نبود .')
                template_name = 'error.html'
        else:
            card.change_status(Card.INPROCESS)
            messages.warning(self.request, 'پرداخت لغو شد .')
            template_name = 'error.html'
        return render(request, f'zarinpal/{template_name}', {})

class CallBackWallet(View):
    def get(self, request, pk):
        if request.GET.get('Status') == 'OK':
            from .models import WalletTransaction
            wallet_tr = get_object_or_404(WalletTransaction.objects.filter(status=0) , pk=pk)
            amount = int(float(wallet_tr.amount))
            client = Client(ZARINPAL_WEBSERVICE)

            result = client.service.PaymentVerification(
                MMERCHANT_ID,
                request.GET.get('Authority'),
                amount,
            )

            if result.Status == 100 or result.Status == 101:
                from django.db.models import F
                wallet_tr.status = result.Status
                wallet_tr.authority = request.GET.get('Authority')
                wallet_tr.save()
                wallet_tr.user.wallet = F('wallet') + wallet_tr.amount
                wallet_tr.user.save()
                template_name = 'success.html'
            else:
                messages.warning(self.request, 'پرداخت موفقیت آمیز نبود .')
                template_name = 'error.html'
        else:
            messages.warning(self.request, 'پرداخت لغو شد .')
            template_name = 'error.html'
        return render(request, f'zarinpal/{template_name}', {})