# from same folder import views
from . import views, views_login
from django.urls import path
from django.contrib.auth import views as auth_login_test

urlpatterns=[
    path('',views.index, name = 'index'),
    path('homepage',views.index, name = 'index'),
    path('register',views.register, name='regiter'),
    path('teacher',views_login.teacher, name='?'),
    path('teacher/home',views_login.teacher, name='teacher'),
    path('login',auth_login_test.login, name='login'),
    path('logout',auth_login_test.logout, name='logout')]