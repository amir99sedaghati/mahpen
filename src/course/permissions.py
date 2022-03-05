from rest_framework.permissions import BasePermission
from zarinpal.models import Pay
from .models import Card
from .exceptions import CourseIdNotNumericException
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class UserHavePaidCardsPermission(BasePermission):
    message = "تا موقعی که سبد خرید های قبلی خود را پرداخت نکرده باشید اجازه اضافه کردن محتوای دیگری را ندارید"

    def has_permission(self, request, view):
        return not Card.objects.filter(is_finished=True, is_paid=False, user=request.user).exists()


class CourseIsPaid(BasePermission):
    message = "شما این کورس را خریداری نکرده اید و اجازه دیدن محتوای آنرا ندارید"

    def get_course_numeric_id_or_raise_exception(self, request):
        course_id = request.META.get("PATH_INFO").split("/")[2]
        if course_id.isnumeric() :
            return int(course_id)
        else :
            raise CourseIdNotNumericException

    def has_permission(self, request, view):
        course_id = self.get_course_numeric_id_or_raise_exception(request=request)
        course_in_card = Pay.objects.filter(status=100,card__user__id=request.user.id, card__courses__id=course_id, card__is_finished=True, card__is_paid=True)
        return course_in_card.count() > 0

class UserActiveCardPermission(BasePermission):
    message = "شما سبد خرید فعالی ندارید"

    def has_permission(self, request, view):
        return not Card.objects.filter(is_finished=False, is_paid=False, user=request.user).exists()