from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def location(request):
    return render(request,'location.html')
def chennai(request):
    return render(request,'chennai.html')
def mumbai(request):
    return render(request,'mumbai.html')


