import django_filters
from .models import Course

class CourseFilterSet(django_filters.FilterSet):
    class Meta(object):
        model = Course
        exclude = [
            'desribe_video',
            'image',
        ]