from django.http import HttpResponse
from django.shortcuts import render
from .models import aboutnew
from .models import picture

def home(request):
    aboutdatanew = aboutnew.objects.get(id = 2)
    picturenew = picture.objects.get(id = 3)
    context = {
        'aboutnew' :aboutdatanew,
        'picture' :picturenew
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')
def product(request):
    return render(request,'product.html')
    