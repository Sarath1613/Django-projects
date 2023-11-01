from django.urls import path
from . import views

urlpatterns = [
    path('',views.teachers,name='teachers'),
    path('attendance/',views.attendents,name='Staffs Attendance'),
    path('timetable/',views.timetable,name='Timetable'),
    

]