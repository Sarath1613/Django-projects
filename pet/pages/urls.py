
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('pricingplan/', views.pricingplan, name='pricingplan'),
    path('theteam/', views.theteam, name='theteam'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('bloggrid/', views.bloggrid, name='bloggrid'),
    path('blogdetails/', views.blogdetails, name='blogdetails'),
    
]
