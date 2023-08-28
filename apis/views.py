from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from elearning.models import Course, Lesson, StudentProgress, Achievement
from .serializers import CourseSerializer, LessonSerializer, StudentProgressSerializer, AchievementSerializer
from rest_framework.response import Response

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class CourseListAPIView(ListAPIView):
    throttle_classes = [UserRateThrottle]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonListAPIView(ListAPIView):
    throttle_classes = [UserRateThrottle]
    def get(self,request):
        lessons = Lesson.objects.all()
        serializer_class = LessonSerializer(lessons,many= True)
        return Response(serializer_class.data)

class StudentProgressListAPIView(ListAPIView):
    throttle_classes = [UserRateThrottle]
    queryset = StudentProgress.objects.all()
    serializer_class = StudentProgressSerializer
    
    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class AchievementListAPIView(ListAPIView):
    throttle_classes = [UserRateThrottle]
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    
    def perform_create(self, serializer):
        serializer.save(student=self.request.user)
