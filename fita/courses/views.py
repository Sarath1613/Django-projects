from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def courses(request):
    return render(request,'courses/courses.html')

def python(request):
    return render(request,'courses/python.html')

def django(request):
    return render(request,'courses/django.html')

def web(request):
    return render(request,'courses/web.html')
