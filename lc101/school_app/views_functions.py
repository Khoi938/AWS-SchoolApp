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