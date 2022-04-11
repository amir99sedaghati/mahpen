from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Card, Course
from .permission import ShouldNotHaveEnableCard
from user_management.permissions import IsAuthenticated
from django.shortcuts import redirect
from . import filtering

class AddCourseToCardView(IsAuthenticated, ShouldNotHaveEnableCard, View):
    card_status_messgage = 'برای اضافه کردن محصول به سبد خرید ابتدا باید سبد خرید در حال پرداخت قبلی را تسویه نمایید، سبد خرید شما بعد از ۱۵ دقیقه به حالت پرداخت نشده باز میگردد .'
    permission_message = 'برای اضافه کردن محصول به سبد خرید ابتدا باید وارد حساب کاربری شوید .'

    def get(self, request, pk, *args, **kwargs):
        past_courses = Course.objects.filter(card__user=self.request.user ,card__status=Card.PAID, id=pk)
        if past_courses.exists():
            pass
        else :
            card, is_created = Card.current_card(request=self.request)
            card.add_course(pk)
        return redirect('course-list')

class DeleteCourseFromCardView(IsAuthenticated, ShouldNotHaveEnableCard, View):
    card_status_messgage = 'برای حذف کردن محصول از سبد خرید ابتدا باید سبد خرید در حال پرداخت قبلی را تسویه نمایید، سبد خرید شما بعد از ۱۵ دقیقه به حالت پرداخت نشده باز میگردد .'
    permission_message = 'برای اضافه کردن محصول به سبد خرید ابتدا باید وارد حساب کاربری شوید .'

    def get(self, request, pk, *args, **kwargs):
        card, is_created = Card.current_card(request=self.request)
        card.delete_course(pk)
        return redirect('course-list')

class CardView(IsAuthenticated, ShouldNotHaveEnableCard, DetailView):
    card_status_messgage = 'برای مشاهده وضعیت سبد خرید ابتدا باید سبد خرید در حال پرداخت قبلی را تسویه نمایید، سبد خرید شما بعد از ۱۵ دقیقه به حالت پرداخت نشده باز میگردد .'
    permission_message = 'برای مشاهده کردن محصول به سبد خرید ابتدا باید وارد حساب کاربری شوید .'
    template_name = 'course/shoppingcart.html'
    context_object_name = 'card'

    def get_object(self, queryset=None) :
        card, is_created = Card.current_card(request=self.request)
        return card

class CoursesView(ListView):
    context_object_name = 'courses'

    def get_queryset(self):
        queryset = Course.objects.all()
        return filtering.CourseFilterSet(data=self.request.GET, queryset=queryset).qs