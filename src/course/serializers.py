from rest_framework import serializers
from . import models
from blog.serializers import CategorySerializer
from django.contrib.auth.models import User
from user_management.serializers import UserSerializer

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    teacher = UserSerializer()

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