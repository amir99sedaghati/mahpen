from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from azbankgateways.exceptions import AZBankGatewaysException
import logging
from django.http import HttpResponse, Http404
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings

from .models import (
    Card,
)

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()

    @action(detail=True , methods=["get"])
    def pay(self , request , pk=None):
        card = get_object_or_404(self.queryset, pk=pk)
        amount = sum([ x.amount - (x.amount * x.off) for x in card.courses.all() ])
        return self.go_to_gateway_view(request, amount , pk)
    
    def go_to_gateway_view(self, request, amount, card_id):
        factory = bankfactories.BankFactory()
        try:
            bank = factory.create()
            bank.set_request(request)
            bank.set_amount(amount)
            bank.set_client_callback_url(reverse('card-paid', args=[card_id]))
            return bank.redirect_gateway()
        except AZBankGatewaysException as e:
            raise e
        
    @action(detail=True , methods=["get"])
    def paid(self , request , pk=None):
        tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
        if not tracking_code:
            raise Http404
        try:
            bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
        except bank_models.Bank.DoesNotExist:
            raise Http404

        if bank_record.is_success:
            return Response({"result" : "پرداخت با موفقیت انجام شد."})

        return Response({"result" : "پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت."})
