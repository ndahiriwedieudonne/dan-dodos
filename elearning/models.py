from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class StudentProgress(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

class Achievement(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()




@receiver(post_save, sender=settings.AUTH_USER_MODEL)

def create_auth_token(sender, instance = None, created = False,**kwargs):
    if created:
        Token.objects.create(User = instance)
