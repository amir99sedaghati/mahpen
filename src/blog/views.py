from rest_framework import viewsets
from django.views.generic import TemplateView
from .models import (
    Category,
    Post,
    Video,
)
from .serializers import (
    CategorySerializer,
    PostSerializer,
    VideoSerializer,
)

class IndexView(TemplateView):
    template_name = 'blog/index.html'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related('category')
    serializer_class = PostSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().select_related('category')
    serializer_class = VideoSerializer
