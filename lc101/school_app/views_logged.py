from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from school_app.models import *
from school_app.views_functions import is_teacher, login_check

def home_redirect(request):
    login_check(request)
    # profile = Profile.objects.get(user = request.user)
    if request.user.profile.is_teacher == True:
        return redirect('/teacher/home')
    else:
        return redirect('/student/home')

        
#------ Teacher's Controller Logic-------

def teacher(request):
    
    if not request.user.is_authenticated:# alt user= User.Objects.filter(username=request.)
        
        messages.warning(request, "Please login or Create an Account.")
        return redirect('login')
    login_check(request)
    if request.user.profile.is_teacher == False:
        messages.warning(request, "You don't have Instructor's Privilege!")
        return redirect('/')
    user = request.user #User.objects.filter(id=request.session['id'])
    return render(request,'teacher/teacher_homepage.html',{'user':user})
    
@login_required
def add_class(request):
    
    # is_teacher(request)
    if request.user.profile.is_teacher == False:
        messages.warning(request, "You don't have Instructor's Privilege!")
        return redirect('/')

    return render(request,'teacher/add_class.html')#,{'user':user})

@login_required #can use request.user.is_authenticated aswell
def student(request):
    
    if 'username' not in request.session:
        return HttpResponse('<h1>Not logged in</h1>')
    else:
        return HttpResponse('<h1>Hello '+request.session['username']+'<h1>')
        
        


# ---- Permission Decorator -----
def is_teacher(user):
    if user.profile.is_teacher:
        return True
    else: 
        return 

# @user_passes_test(is_teacher)
#--------------------------------
