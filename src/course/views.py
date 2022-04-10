from django.views.generic.base import View
from django.views.generic.detail import DetailView
from .models import Card
from .permission import ShouldNotHaveEnableCard

class AddCourseToCardView(ShouldNotHaveEnableCard):
    permission_message = 'برای اضافه کردن محصول به سبد خرید ابتدا باید سبد خرید در حال پرداخت قبلی را تسویه نمایید، سبد خرید شما بعد از ۱۵ دقیقه به حالت پرداخت نشده باز میگردد .'

    def get(self, request, pk, *args, **kwargs):
        pass

class DeleteCourseFromCardView(ShouldNotHaveEnableCard):
    permission_message = 'برای حذف کردن محصول از سبد خرید ابتدا باید سبد خرید در حال پرداخت قبلی را تسویه نمایید، سبد خرید شما بعد از ۱۵ دقیقه به حالت پرداخت نشده باز میگردد .'

    def get(self, request, pk, *args, **kwargs):
        pass

class CardView(ShouldNotHaveEnableCard, DetailView):
    permission_message = 'برای مشاهده وضعیت سبد خرید ابتدا باید سبد خرید در حال پرداخت قبلی را تسویه نمایید، سبد خرید شما بعد از ۱۵ دقیقه به حالت پرداخت نشده باز میگردد .'
    template_name = 'course/shoppingcart.html'
    queryset = Card.objects.filter(status=Card.INPROCESS).prefetch_related('courses')
    context_object_name = 'card'

    def get_object(self, queryset=None) :
        return self.queryset.get_or_create(user=self.request.user)[0]
