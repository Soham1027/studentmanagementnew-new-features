"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .import hod_views,views,staff_views,student_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.LOGIN, name="login"),
   
    path('logout/',views.Logoutpage, name='logout'),
    #home
    path('student_home',student_views.student_home,name='student_home'),
    path('hod_home',hod_views.hod_home,name='hod_home'),
    path('staff_home',staff_views.staff_home,name='staff_home'),
  
   
    #profile
    path('profile',views.profile, name='profile'),
    path('profileupdate',views.profileupdate, name='profileupdate'),
    # path('accounts/login/', views.LOGIN, name="login"),
    path("viewstaffbasemain/", views.BASE, name="basemain"),
    path('doLogin',views.doLogin,name='doLogin'), # type: ignore
    #hod
    #subject
    path('student',student_views.mainsubject,name='student'),
   #timetable
    path('addtimetable',staff_views.add_timetable,name='addtimetable'),
    path('viewtimetable',staff_views.view_timetable,name='viewtimetable'),
    path('<int:id>',staff_views.add_timetable,name='updatett'),
    path('delete/<int:id>',staff_views.delete_timetable,name='deletett'),
    path('viewtimetablestudent',staff_views.view_timetable_student,name='viewtimetablestudent'),
 
    
    #staff
    path('addstaff',hod_views.add_staff,name='addstaff'),
    path('viewstaff',hod_views.view_staff,name='viewstaff'),
    path('editstaff/<str:id>',hod_views.edit_staff,name='editstaff'),
    path('updatestaff',hod_views.update_staff,name='updatestaff'),
    path('deletestaff/<str:admin>',hod_views.delete_staff,name='deletestaff'),
    path('viewstaffadmin',hod_views.view_staff_admin,name='viewstaffadmin'),
    
   
   
   
   
   #student
    path('addstudent',staff_views.add_student,name='addstudent'),
    path('student_list',staff_views.student_list,name='student_list'),
    path('studentedit/<str:id>',staff_views.student_edit,name='studentedit'),
    path('studentupdate',staff_views.studentupdate,name='studentupdate'),
    path('studentdelete/<str:admin>',staff_views.studentdelete,name='studentdelete'),
    path('student_list_admin',staff_views.student_list_admin,name='student_list_admin'),
   
   
   
    #change password
    path('change_password',auth_views.PasswordChangeView.as_view(template_name='change_password.html',success_url='/'),name='change_password'),
    #email
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
      
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
  
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
  
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),   
  


  
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)