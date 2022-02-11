from django.http import HttpResponse
from django.shortcuts import redirect
from suds.client import Client
from mahpen.settings import ZARINPAL_CONFIGURATION
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Pay
from .serializers import PaySerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from course.models import Card

MMERCHANT_ID = ZARINPAL_CONFIGURATION.get("merchant_id")
ZARINPAL_WEBSERVICE = ZARINPAL_CONFIGURATION.get("zarinpal_webservice")
DESCRIPTION = ZARINPAL_CONFIGURATION.get("description")
CALL_BACK_URL = ZARINPAL_CONFIGURATION.get("call_back_url")
# return HttpResponseRedirect(redirect_to='https://google.com')

class PayViewSet(ModelViewSet):
    queryset = Pay.objects.all()
    serializer_class = PaySerializer

    @action(detail=True , methods=["get"])
    def pay(self, request, pk=None):
        card = get_object_or_404(Card.objects.all().prefetch_related('courses') , pk=pk)
        serializer = PaySerializer(data={**request.data , 'card' : card.id})
        if serializer.is_valid() :
            return self.send_request(self.create_user_data_dictionary(serializer, card))
        return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
    
    def create_user_data_dictionary(self, serializer, card):
        amount = sum([ x.amount - (x.amount * ( x.off / 100 )) for x in card.courses.all() ])
        phone_number = serializer.data.get("phone_number")
        email = serializer.data.get("email")
        call_back_parameter = ''
        if phone_number :
            call_back_parameter += f'phone_number={phone_number}'
        if email :
            if phone_number :
                call_back_parameter += f'&email={email}'
            else :
                call_back_parameter += f'email={email}'

        return {
            "phone_number" : phone_number,
            "email" : email,
            "amount" : amount ,
            "call_back_url" : F'{CALL_BACK_URL}/card/{card.id}/verify/?{call_back_parameter}',
        }

    def send_request(self, user_data_dictionary):
        client = Client(ZARINPAL_WEBSERVICE)
        result = client.service.PaymentRequest(MMERCHANT_ID,
                                            user_data_dictionary.get("amount"),
                                            DESCRIPTION,
                                            user_data_dictionary.get("email"),
                                            user_data_dictionary.get("phone_number"),
                                            user_data_dictionary.get("call_back_url"))
        if result.Status == 100:
            # return redirect('https://www.zarinpal.com/pg/StartPay/' + result.Authority)
            return redirect('https://sandbox.zarinpal.com/pg/StartPay/' + result.Authority)
        else:
            return Response({'status' , 'شما تنظیمات درگاه زرین پال را به درستی انجام نداده اید'},
                    status=status.HTTP_502_BAD_GATEWAY)

    @action(detail=True , methods=["get"])
    def verify(self, request, pk=None):
        card = get_object_or_404(Card.objects.all().prefetch_related('courses') , pk=pk)
        amount = sum([ x.amount - (x.amount * ( x.off / 100 )) for x in card.courses.all() ])
        client = Client(ZARINPAL_WEBSERVICE)
        if request.GET.get('Status') == 'OK':
            result = client.service.PaymentVerification(MMERCHANT_ID,
                                                        request.GET['Authority'],
                                                        amount)
            if result.Status == 100:
                return HttpResponse('Transaction success. RefID: ' + str(result.RefID))
            elif result.Status == 101:
                return HttpResponse('Transaction submitted : ' + str(result.Status))
            else:
                return HttpResponse('Transaction failed. Status: ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed or canceled by user')