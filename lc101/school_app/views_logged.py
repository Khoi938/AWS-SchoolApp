from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from school_app.models import *

@login_required
def home_redirect(request):
    profile = Profile.objects.get(user = request.user)
    if profile.is_teacher == True:
        return redirect('/teacher/home')
        #return render(request,'teacher/teacher_homepage.html')
    else:
        return redirect('/student/home')
        #return HttpResponse('<h1>Hello '+request.session['username']+'<h1>')
        
#------ Teacher's Controller Logic-------
@login_required
def teacher(request):
    
    return render(request,'teacher/teacher_homepage.html')
    
@login_required
def add_class(request):
    
    return render(request,'teacher/add_class.html')

@login_required #can use request.user.is_authenticated aswell
def student(request):
    
    if 'username' not in request.session:
        return HttpResponse('<h1>Not logged in</h1>')
    else:
        return HttpResponse('<h1>Hello '+request.session['username']+'<h1>')
