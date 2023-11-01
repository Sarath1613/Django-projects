from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def locations(request):
    return render(request,'locations/location.html')

def annanagar(request):
    return render(request,'locations/annanagar.html')

def velacherry(request):
    return render(request,'locations/velacherry.html')

def tambaram(request):
    return render(request,'locations/tambaram.html')
