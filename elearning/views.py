from django.shortcuts import render
from .models import Course

def index(request):
    posts = Course.objects.all()
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def progress(request):
    return render(request, 'progress.html')
# Create your views here.
