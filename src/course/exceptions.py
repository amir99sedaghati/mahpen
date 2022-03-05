from rest_framework.exceptions import APIException

class CourseIdNotNumericException(APIException):
    status_code = 400
    default_detail = 'آیدی کورس حتما باید عددی باشد'
    default_code = 'bad_request'

