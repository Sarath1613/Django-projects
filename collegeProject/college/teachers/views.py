from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def teachers(request):
    return render (request,'teachers/teachers.html')

def attendents(request):
    return render (request,'teachers/attendance.html')

def timetable (request):
    return render (request,'teachers/timetable.html')

