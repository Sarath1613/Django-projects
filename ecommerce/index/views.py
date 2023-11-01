from django.http import HttpResponse
from django.shortcuts import render
from .models import offers
from .models import picture
from .models import client
from .models import contactform

def home(request):
    newoffers = offers.objects.get(id = 1)
    newpicture = picture.objects.get(id = 1)
    clientdata = client.objects.all()
    context = {
        'offers' : newoffers,
        'picture': newpicture,
        'client' : clientdata,
    }


    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contactformdata=contactform(name=name,email=email,subject=subject,message=message)
        contactformdata.save()


    return render(request,'contact.html')
def cart(request):
    return render(request,'cart.html')