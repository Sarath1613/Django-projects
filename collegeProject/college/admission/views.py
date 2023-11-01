from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def admission(request):
    return render (request,'admission/admission.html')

def counsling(request):
    return render (request,'admission/counselling.html')

def management(request):
    return render (request,'admission/management.html')

def nri (requests):
    return render (requests,'admission/nri.html')
 