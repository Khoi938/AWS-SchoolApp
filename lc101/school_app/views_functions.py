from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from school_app.models import *
# ----- Custom Functions goes Here -----

# Check to see if user is login add message
def is_login(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login or Create an Account.")
        return False
    return True
    
# Check to see if a User is a Teacher
def is_teacher(request): 
    if request.user.profile.is_teacher == False:
        messages.warning(request, "You don't have Instructor's Privilege!")
        return False
    return True
    
# Add Class to Student and Check number of current class
def add_class(request, student, subject):
        if student.enrolled.count() >= 7:#Count hit DB return with num, len(s) pull the entire list out and count it.
            messages.warning(request,'Student cannot be enrolled in more than 7 Class')
            return False
        else:
            student.enrolled.add(subject)
            return True
