from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    #views Data
    # path('',views.dashboard),
    path('dashboard',views.dashboard,name='dashboard'),
    path('index',views.index),
    path('student',views.st,name='student'),
    path('standard',views.standard,name='standard'),
    path('faculty',views.Facu,name='faculty'),
    path('subject',views.subj,name='subject'),
    path('timetable',views.timetab,name='timetable'),
    path('atten_student',views.studatt,name='atten_student'),
    path('atten_faculty',views.attenfac,name='atten_faculty'),
    path('login_admin/' ,views.admin_login , name="admin_login"),

   #Adding Data.
    path('addstandard',views.addstandard),
    path('addsubject',views.addsubject),
    path('addstudent',views.addstudent),
    path('addfaculty',views.addfaculty),
    path('addattfac',views.addattfac),
    path('addattstu',views.addattstu),
    path('addtimetable',views.addtimetable),

    
    #Update Data.
    path('editstandard/<int:edit_id>',views.editstandard,name="editstandard"),
    path('editsubject/<int:edit_id>/', views.editsubject, name='editsubject'),
    path('editStudent/<int:id>/', views.editStudent, name='editStudent'),
    path('editfaculty/<int:edit_id>/', views.editfaculty, name='editfaculty'),
    path('edittimetable/<int:id>/', views.edittimetable, name='edittimetable'),
    path('editattefac/<int:id>/', views.editattefac, name='editattefac'),
    path('editattestu/<int:id>/', views.editattestu, name='editattestu'),

    #Delete Data.
    path('sta_delete/<int:delete_id>',views.sta_delete,name="sta_delete"),
    path('sub_delete/<int:delete_id>',views.sub_delete,name="sub_delete"),
    path('s_delete/<int:delete_id>',views.s_delete,name="s_delete"),
    path('fac_delete/<int:delete_id>',views.fac_delete,name="fac_delete"),
    path('timetable_delete/<int:delete_id>',views.timetable_delete,name="timetable_delete"),
    path('attenfac_delete/<int:delete_id>',views.attenfac_delete,name="attenfac_delete"),
    path('attenstu_delete/<int:delete_id>',views.attestu_delete,name="attenstu_delete"),

    #student side
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('Home/', views.Home_view, name='Home'),
    path('register/', views.register, name='register'),
    path('welcome/', views.welcome, name='welcome'),  
    
    #standrd page links
    path('six/', six_view, name='six'),  
    path('seven_view/', seven_view, name='seven_view'), 
    path('eight_view/', eight_view, name='eight_view'), 
    path('nine_view/', nine_view, name='nine_view'),
    path('ten_view/', ten_view, name='ten_view'),


]

#file uplode
path('standards/', Standard, name='standard_list'),  # Adjust as 



