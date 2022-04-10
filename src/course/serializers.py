from rest_framework import serializers
from . import models
from blog.serializers import CategorySerializer
from django.contrib.auth.models import User

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.Course
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)
    class Meta:
        model = models.Card
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = models.Content
        fields = '__all__'