from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pricingplan(request):
    return render(request,'pages/pricingplan.html')
def theteam(request):
    return render(request,'pages/theteam.html')
def testimonials(request):
    return render(request,'pages/testimonials.html')
def bloggrid(request):
    return render(request,'pages/bloggrid.html')
def blogdetails(request):
    return render(request,'pages/blogdetails.html')