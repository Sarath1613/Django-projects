from django.http import HttpResponse    
from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def games(request):
    return render(request,'games.html')
def forums(request):
    return render(request,'forums.html')