from django.http import HttpResponse 
from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def degree(request):
    return render(request,'degree.html')

