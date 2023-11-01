from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def students(request):
    return render(request,'students/students.html')

def attendents(request):
    return render(request,'students/attendance.html')

def examination(request):
    return render(request,'students/examination.html')

def results(request):
    return render(request,'students/results.html')
 