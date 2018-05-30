from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from school_app.models import *



@login_required
def home_redirect(request):
    profile = Profile.objects.get(user = request.user)
    if profile.is_teacher == True:
        return redirect('/teacher/home')
    else:
        return redirect('/student/home')

        
#------ Teacher's Controller Logic-------

@login_required
def teacher(request):
    user = User.objects.filter(id=request.session['id'])
    return render(request,'teacher/teacher_homepage.html',{'user':user})
    
@login_required
def add_class(request):
    is_teacher(request)
    if request.user.profile.is_teacher == False:
        messages.warning(request, "You don't have Instructor's Privilege!")
        return render(request,'homepage/error.html')

    return render(request,'teacher/add_class.html')

@login_required #can use request.user.is_authenticated aswell
def student(request):
    
    if 'username' not in request.session:
        return HttpResponse('<h1>Not logged in</h1>')
    else:
        return HttpResponse('<h1>Hello '+request.session['username']+'<h1>')
        
        


#---- Permission Decorator -----
# def is_teacher(user):
#     if user.profile.is_teacher:
#         return True
#     else: 
#         return False

# @user_passes_test(is_teacher)
#--------------------------------
