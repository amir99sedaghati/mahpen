from url_filter.filtersets import ModelFilterSet
from .models import Post

class CourseFiltering(ModelFilterSet):
    class Meta(object):
        model = Post