from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def shop(request):
    return render(request,'shop/shop.html')
def wishlist(request):
    return render(request,'shop/wishlist.html')
def singleproduct(request):
    return render(request,'shop/singleproduct.html')
def cart(request):
    return render(request,'shop/cart.html')
def checkout(request):
    return render(request,'shop/checkout.html')
