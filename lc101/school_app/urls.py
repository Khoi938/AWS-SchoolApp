# from same folder import views
from . import views, views_logged
from django.urls import path
from django.contrib.auth import views as auth_login_test

urlpatterns=[
    path('',views.index, name = 'index'),
    path('homepage',views.index, name = 'homepage'),
    path('register',views.register, name='register'),
    
    #when user visit this address, call this function
    path('teacher',views_logged.teacher, name='teacher'),
    path('teacher/home',views_logged.teacher, name='teacher_home'),
    path('teacher/add_class',views_logged.add_class, name='add_class'),
    
    path('teacher/edit_class', views_logged.edit_class, name='edit_class'),
    path('teacher/edit_class/<int:class_id>/', views_logged.edit_class, name='edit_class'),
    path('teacher/student_list', views_logged.student_list, name='student_list'),
    
    path('teacher/student_views', views_logged.student_views, name='student_views'),
    path('teacher/student_views/<int:student_id>/', views_logged.student_views, name='student_views'),
    
    path('student',views_logged.student,name='student'),
    path('student/home',views_logged.student,name='student_home'),
    
    path('home_redirect',views_logged.home_redirect, name = 'home_redirect'),
    path('login',views.login, name='login'),
    path('logout',views_logged.logout, name='logout')]