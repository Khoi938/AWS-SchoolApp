from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from school_app.models import *
from school_app.views_functions import is_teacher, is_login

        
#------ Teacher's Controller Logic-------

def teacher(request):
    if is_login(request) == False: # Check for login/ add message 'please login'
        return redirect('/login')
    if is_teacher(request) == False:
        return redirect('/')
    subjects=Subject.objects.filter(teacher=request.user.teacher)
    return render(request,'teacher/teacher_homepage.html',{'subjects':subjects})
    

def add_class(request):
    if is_login(request) == True:
        if request.user.profile.is_teacher == False:
            messages.warning(request, "You don't have Instructor's Privilege!")
            return redirect('/')
        elif request.method == 'POST':
            subject_name = request.POST['subject_name']
            description = request.POST['description']
            teacher = request.user.teacher
            added_class = Subject.objects.create(teacher=teacher,subject_name=subject_name, description=description)
            messages.success(request, 'Subject: '+added_class.subject_name+' Instructor: '+ 
            request.user.get_full_name()+ ' has been created.' )
            return render(request,'teacher/add_class.html')
        else:
            return render(request,'teacher/add_class.html')
            

def edit_class(request,class_id):
    if is_login(request) == True:
        if request.user.profile.is_teacher == False:
            messages.warning(request, "You don't have Instructor's Privilege!")
            return redirect('/')
        elif request.method == 'POST':
            x=3
        else:
            edit_class=Subject.objects.filter(id=int(class_id))
            return render(request,'teacher/edit_class.html',{'edit_class':edit_class})
            
@login_required
def student(request):
    
    if 'username' not in request.session:
        return HttpResponse('<h1>Not logged in</h1>')
    else:
        return HttpResponse('<h1>Hello '+request.user.username+'<h1>')
        
#----- Logout -----
def logout(request):
    if is_login(request) == False: 
        return redirect('/homepage')
    full_name = request.user.get_full_name()
    messages.success(request, full_name + ' have logged out.')
    auth_logout(request)
    return render(request,'homepage/index.html') 

#----- Redirect User to different homepage -----
def home_redirect(request):
    login_check(request)
    if request.user.profile.is_teacher == True:
        return redirect('/teacher/home')
    else:
        return redirect('/student/home')

