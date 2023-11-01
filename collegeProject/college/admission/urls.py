
from django.urls import path
from . import views

urlpatterns = [
    path('',views.admission,name='admission'),
    path('counselling/',views.counsling,name='counselling'),
    path('management/',views.management,name='management'),
    path('nri/',views.nri,name='NRI'),

]