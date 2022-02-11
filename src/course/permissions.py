from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException
from zarinpal.models import Pay

class CourseIdNotNumericException(APIException):
    status_code = 400
    default_detail = 'آیدی کورس حتما باید عددی باشد'
    default_code = 'bad_request'

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
        course_in_card = Pay.objects.filter(status=100, card__courses__id=course_id, card__is_finished=True, card__is_paid=True)
        return course_in_card.count() > 0