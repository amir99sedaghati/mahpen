from rest_framework import serializers
from . import models
from blog.serializers import CategorySerializer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        ]

class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    teacher = UserSerializer()

    class Meta:
        model = models.Course
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = models.Content
        fields = '__all__'