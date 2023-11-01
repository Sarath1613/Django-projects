
from django.urls import path
from . import views

urlpatterns = [
  
    path('location/', views.location,name= 'location'),
    path('chennai/', views.chennai,name= 'chennai'),
    path('mumbai/', views.mumbai,name= 'mumbai'),
    
]
