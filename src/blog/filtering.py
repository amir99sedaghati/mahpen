from url_filter.filtersets import ModelFilterSet
from .models import Post, Video

class PostFiltering(ModelFilterSet):
    class Meta(object):
        model = Post

class VideoFiltering(ModelFilterSet):
    class Meta(object):
        model = Video