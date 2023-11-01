from django.urls import path,include
from . import views
urlpatterns = [
    
    path('', views.locations,name='locations'),
    path('annanagar/', views.annanagar,name='annanagar'),
    path('velacherry/', views.velacherry,name='velacherry'),
    path('tambaram/', views.tambaram,name='tambaram'),
    


]
