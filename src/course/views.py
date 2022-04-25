from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from .models import Card, Course
from .permission import ShouldNotHaveEnableCard
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from . import filtering
from django.shortcuts import redirect

class AddCourseToCardView(LoginRequiredMixin, ShouldNotHaveEnableCard, View):
    card_status_messgage = 'برای اضافه کردن محصول به سبد خرید ابتدا باید سبد خرید در حال پرداخت قبلی را تسویه نمایید، سبد خرید شما بعد از ۱۵ دقیقه به حالت پرداخت نشده باز میگردد .'
    
    def get(self, request, pk, *args, **kwargs):
        return redirect('course-detail', pk)

    def post(self, request, pk, *args, **kwargs):
        course = get_object_or_404(Course.objects.filter(id=pk))
        if not course.is_in_user_paid_card(self.request):
            card, is_created = Card.current_card(request=self.request)
            card.add_course(course)
            messages.warning(self.request , "دوره با موفقیت به سبد خرید اضافه شد .")
        else :
            messages.warning(self.request , "شما قبلا این دوره را خریداری کرده اید . برای دیدن محتوای آن میتوانید به پروفایل خود مراجعه کنید .")
        return redirect('course-list')

class DeleteCourseFromCardView(LoginRequiredMixin, ShouldNotHaveEnableCard, View):
    card_status_messgage = 'برای حذف کردن محصول از سبد خرید ابتدا باید سبد خرید در حال پرداخت قبلی را تسویه نمایید، سبد خرید شما بعد از ۱۵ دقیقه به حالت پرداخت نشده باز میگردد .'

    def get(self, request, pk, *args, **kwargs):
        return redirect('course-detail', pk)

    def post(self, request, pk, *args, **kwargs):
        course = get_object_or_404(Course.objects.filter(id=pk))
        card, is_created = Card.current_card(request=self.request)
        card.delete_course(course)
        return redirect('card-detail')

class CardView(LoginRequiredMixin, ShouldNotHaveEnableCard, DetailView):
    card_status_messgage = 'برای مشاهده وضعیت سبد خرید ابتدا باید سبد خرید در حال پرداخت قبلی را تسویه نمایید، سبد خرید شما بعد از ۱۵ دقیقه به حالت پرداخت نشده باز میگردد .'
    template_name = 'course/shoppingcart.html'
    context_object_name = 'card'

    def get_object(self, queryset=None) :
        card, is_created = Card.current_card(request=self.request)
        return card

class CoursesView(ListView):
    context_object_name = 'courses'
    paginate_by = 16

    def get_queryset(self):
        qs = filtering.CourseFiltering(data=self.request.GET, queryset=Course.objects.all().order_by('-id')).filter()
        return filtering.ordering(qs, self.request)
    
    def get_context_data(self, **kwargs):
        from blog.models import Category
        context = super().get_context_data(**kwargs)
        context['most_sales'] = Course.get_most_sales()
        context['newest_course'] = Course.get_newest_course()
        context['categotories'] = Category.objects.all()
        return context

class CourseDetailView(DetailView):
    context_object_name = 'course'
    queryset = Course.objects.filter(is_expire=False).prefetch_related('teacher', 'category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = context['course']
        if self.request.user.is_authenticated :
            context['carded_course'] = course.is_in_user_card(self.request)
            context['buyed_course'] = course.is_in_user_paid_card(self.request)
        return context