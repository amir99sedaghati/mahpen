from rest_framework import viewsets
from .models import (
    Category,
    Post,
)
from .serializers import (
    CategorySerializer,
    PostSerializer,
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related('category')
    serializer_class = PostSerializer
