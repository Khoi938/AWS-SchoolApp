# from same folder import views
from . import views, views_logged
from django.urls import path
from django.contrib.auth import views as auth_login_test

urlpatterns=[
    path('',views.index, name = 'index'),
    path('homepage',views.index, name = 'index'),
    path('register',views.register, name='register'),
    #when user visit this address, call this function
    path('teacher',views_logged.teacher, name='teacher'),
    path('teacher/home',views_logged.teacher, name='teacher_home'),
    path('student',views_logged.student,name='student'),
    path('student/home',views_logged.student,name='student_home'),
    
    path('split',views_logged.home_redirect, name = 'home_redirect'),
    path('login',auth_login_test.login, name='login'),
    path('logout',auth_login_test.logout, name='logout')]