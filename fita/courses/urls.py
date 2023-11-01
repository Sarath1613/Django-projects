
from django.urls import path
from . import views
urlpatterns = [
 
    path('', views.courses,name='courses'),
    path('django/', views.django,name='django'),
    path('python/', views.python,name='python'),
    path('web/', views.web,name='web'),


]