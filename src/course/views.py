from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from . import serializers
from .permissions import (
    CourseIsPaid,
    UserHavePaidCardsPermission,
    UserActiveCardPermission,
)
from rest_framework.permissions import IsAuthenticated
from .models import (
    Course,
    Content,
    Card,
)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer

    def get_content_queryset(self, course_id):
        return Content.objects.filter(course__id=course_id)

    def get_content_serializer(self):
        return serializers.ContentSerializer

    
    @action(detail=False , methods=["get"], url_path='(?P<course_id>[^/.]+)/content', permission_classes=[IsAuthenticated, CourseIsPaid])
    def get_content(self, request, course_id=None):
        contents = self.get_content_queryset(course_id)
        serializer = self.get_content_serializer()(contents, many=True)
        return Response(serializer.data)

    @action(detail=False , methods=["get"], url_path='(?P<course_id>[^/.]+)/content/(?P<video_id>[^/.]+)', permission_classes=[IsAuthenticated, CourseIsPaid])
    def get_special_content(self, request, course_id=None, video_id=None):
        content = get_object_or_404(self.get_content_queryset(course_id).filter(id=video_id))
        serializer = self.get_content_serializer()(content, many=False)
        return Response(serializer.data)

class CardViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CardSerializer
    course_queryset = Course.objects.all()

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)


    @action(detail=False , methods=["get"], url_path='add-course/(?P<course_id>[^/.]+)', permission_classes=[IsAuthenticated, UserHavePaidCardsPermission])
    def add_course_to_card(self, request, course_id=None):
        course = get_object_or_404(self.course_queryset.filter(id=course_id))
        card = Card.objects.get_or_create(
            user = request.user ,
            is_finished = False ,
            is_paid = False ,
        )[0]
        card.courses.add(course)
        return Response({"status" : "ok"})

    @action(detail=False , methods=["get"], url_path='del-course/(?P<course_id>[^/.]+)', permission_classes=[IsAuthenticated, UserActiveCardPermission])
    def del_course_from_card(self, request, course_id=None):
        course = get_object_or_404(self.course_queryset.filter(id=course_id))
        card = get_object_or_404(Card.objects.filter(
            user = request.user ,
            is_finished = False ,
            is_paid = False ,
        ))
        card.courses.remove(course)
        return Response({"status" : "ok"})

