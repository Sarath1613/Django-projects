from django.http import HttpResponse
from django.shortcuts import render
from .models import contactform

def home(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contactformdata=contactform(name=name,email=email,subject=subject,message=message)
        contactformdata.save()

    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def resume(request):
    return render(request,'resume.html')
def portfolio(request):
    return render(request,'portfolio.html')
def contact(request):
    return render(request,'contact.html')