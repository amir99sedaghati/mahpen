from url_filter.filtersets import ModelFilterSet
from .models import Course

class CourseFiltering(ModelFilterSet):
    class Meta(object):
        model = Course

def ordering(qs, request):
    try :
        return qs.order_by(request.GET.get('ordering', '-id'))
    except :
        return qs
