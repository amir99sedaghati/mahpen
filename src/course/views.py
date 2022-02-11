from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from . import serializers
from .permissions import CourseIsPaid
from .models import (
    Course,
    Content,
)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer

    def get_content_queryset(self, course_id):
        return Content.objects.filter(course__id=course_id)

    def get_content_serializer(self):
        return serializers.ContentSerializer

    
    @action(detail=False , methods=["get"], url_path='(?P<course_id>[^/.]+)/content', permission_classes=[CourseIsPaid])
    def get_content(self, request, course_id=None):
        contents = self.get_content_queryset(course_id)
        serializer = self.get_content_serializer()(contents, many=True)
        return Response(serializer.data)

    @action(detail=False , methods=["get"], url_path='(?P<course_id>[^/.]+)/content/(?P<video_id>[^/.]+)', permission_classes=[CourseIsPaid])
    def get_special_content(self, request, course_id=None, video_id=None):
        content = get_object_or_404(self.get_content_queryset(course_id).filter(id=video_id))
        serializer = self.get_content_serializer()(content, many=False)
        return Response(serializer.data)