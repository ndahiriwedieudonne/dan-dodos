

from django.urls import path
from . import views
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    # ... (swagger configuration remains the same)
)

urlpatterns = [
     path('course_admin/', admin.site.urls,name='course_admin'),
    path("Course/", views.CourseListAPIView.as_view(), name="Course"),
    path("Lesson/", views.LessonListAPIView.as_view(), name="Lesson"),
    path("StudentProgress/", views.StudentProgressListAPIView.as_view(), name="StudentProgress"),
    path("Achievement/", views.AchievementListAPIView.as_view(), name="Achievement"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
