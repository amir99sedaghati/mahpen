from django.shortcuts import redirect
from suds.client import Client
from mahpen.settings import ZARINPAL_CONFIGURATION
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from .models import Pay
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from course.models import Card

MMERCHANT_ID = ZARINPAL_CONFIGURATION.get("merchant_id")
ZARINPAL_WEBSERVICE = ZARINPAL_CONFIGURATION.get("zarinpal_webservice")
DESCRIPTION = ZARINPAL_CONFIGURATION.get("description")
CALL_BACK_URL = ZARINPAL_CONFIGURATION.get("call_back_url")
# return HttpResponseRedirect(redirect_to='https://google.com')

class PayViewSet(ViewSet):
    card_queryset = Card.objects.all().prefetch_related('courses')

    @action(detail=True , methods=["get"], permission_classes=[IsAuthenticated])
    def pay(self, request, pk=None):
        card = get_object_or_404(self.card_queryset.filter(is_paid=False) , pk=pk)
        card.__class__.objects.update(
            is_finished=True,
        )
        return self.send_request(self.create_user_data_dictionary(request, card))
    
    def create_user_data_dictionary(self, request , card):
        amount = sum([ x.amount - (x.amount * ( x.off / 100 )) for x in card.courses.all() ])
        return {
            "email" : request.user.email,
            "amount" : amount ,
            "call_back_url" : F'{CALL_BACK_URL}/card/{card.id}/verify/?email={request.user.email}',
        }

    def send_request(self, user_data_dictionary):
        client = Client(ZARINPAL_WEBSERVICE)
        result = client.service.PaymentRequest(MMERCHANT_ID,
                                            user_data_dictionary.get("amount"),
                                            DESCRIPTION,
                                            user_data_dictionary.get("email"),
                                            None,
                                            user_data_dictionary.get("call_back_url"))
        if result.Status == 100:
            # return redirect('https://www.zarinpal.com/pg/StartPay/' + result.Authority)
            return redirect('https://sandbox.zarinpal.com/pg/StartPay/' + result.Authority)
        else:
            return Response({'status' , 'شما تنظیمات درگاه زرین پال را به درستی انجام نداده اید'},
                    status=status.HTTP_502_BAD_GATEWAY)

    @action(detail=True , methods=["get"])
    def verify(self, request, pk=None):
        card = get_object_or_404(self.card_queryset.filter(is_finished=True) , pk=pk)
        amount = sum([ x.amount - (x.amount * ( x.off / 100 )) for x in card.courses.all() ])
        client = Client(ZARINPAL_WEBSERVICE)
        if request.GET.get('Status') == 'OK':
            result = client.service.PaymentVerification(MMERCHANT_ID,
                                                        request.GET.get('Authority'),
                                                        amount)
            
            Pay.objects.create(
                card = card ,
                amount = amount ,
                email = request.GET.get('email') ,
                status = result.Status ,
                authority = request.GET.get('Authority') ,
            )

            if result.Status == 100 or result.Status == 101:
                card.__class__.objects.update(
                    is_paid = True ,
                )
                return Response({'status' : 'تراکنش موفقیت آمیز بود'} , status=status.HTTP_200_OK)
            else:
                return Response({'status' : 'تراکنش موفقیت آمیز نبود'} , status=status.HTTP_402_PAYMENT_REQUIRED)
        else:
            return Response({'status' : 'تراکنش توسط پرداخت کننده لفو شده است'} , status=status.HTTP_410_GONE)