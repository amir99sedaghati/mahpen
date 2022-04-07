from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = models.Post
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = models.Video
        fields = '__all__'

