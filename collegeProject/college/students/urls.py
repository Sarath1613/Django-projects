from django.urls import path
from . import views

urlpatterns = [
    path('',views.students,name='Students'),
    path('attendance/',views.attendents,name='Attendance'),
    path('examination/',views.examination,name='Examinations'),
    path('result/',views.results,name='Results'),

]