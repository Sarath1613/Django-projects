from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render (request,'index.html')

def about(request):
    return render (request,'about.html')

def services(request):
    return render (request,'services.html')

def contact(request):
    return render (request,'contact.html')

def projects(request):
    return render (request,'projects.html')

def blog(request):
    return render(request,'blog.html')