from django.shortcuts import redirect
from django.urls import reverse
from suds.client import Client
from .models import Pay
from django.shortcuts import get_object_or_404
from course.models import Card
from django.views.generic.base import View
from user_management import handlers
from django.http.response import HttpResponse
from .configurations import *
from user_management.permissions import IsAuthenticated

class PayView(IsAuthenticated, View):
    permission_message = 'برای پرداخت ابتدا باید حساب کاربری خودتان شوید .'

    def card_queryset(self):
        return Card.objects.filter(user=self.request.user)

    def get(self, request, pk, *arg, **kwargs):
        card = get_object_or_404(self.card_queryset().exclude(status=Card.PAID) , pk=pk)
        card.change_status(Card.FREEZE)
        return self.send_request(card)

    def send_request(self, card):
        call_back_url = reverse('card-pay' , args=card.id)
        client = Client(ZARINPAL_WEBSERVICE)
        result = client.service.PaymentRequest(
            MMERCHANT_ID,
            card.calculate_amount(),
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
    
    def get(self, request, pk=None):
        card = get_object_or_404(self.card_queryset().filter(status=Card.FREEZE) , pk=pk)
        if request.GET.get('Status') == 'OK':
            amount = int(float(request.GET.get('amount')))
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
                # TODO : make valid message and template_name
                return HttpResponse()
            else:
                card.change_status(Card.INPROCESS)
                HttpResponse()
        else:
            card.change_status(Card.INPROCESS)
            HttpResponse()