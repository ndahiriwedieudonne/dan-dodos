# from django.contrib import admin
# from .models import Lesson, Course

# # @admin.register(Lesson)
# # class LessonAdmin(admin.ModelAdmin):
# #     list_display=('title')

# class CourseAdmi(admin.ModelAdmin):
#    model = Course
#    fields = ["title","desc","lessons"]
# admin.site.register(Course,CourseAdmi)

# class LessonAdmi(admin.ModelAdmin):
#    model = Lesson
#    fields = ["name"]
# admin.site.register(Lesson,LessonAdmi)

# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display=('title','desc','lesson')            

# Register your models here.


from django.contrib import admin
from .models import Course, Lesson, StudentProgress, Achievement

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor')
    search_fields = ('title', 'instructor__username')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    list_filter = ('course',)
    search_fields = ('title', 'course__title')

@admin.register(StudentProgress)
class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'lesson', 'completed')
    list_filter = ('student', 'lesson', 'completed')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('student', 'title')
    list_filter = ('student',)
    search_fields = ('title',)
