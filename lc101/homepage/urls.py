# from same folder import views
from . import views
from django.urls import path

urlpatterns=[
    path('',views.index, name = 'huh?')]