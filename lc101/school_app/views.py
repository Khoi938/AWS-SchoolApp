from django.shortcuts import render, redirect
from django.http import HttpResponse

from school_app.models import *
from school_app.views_functions import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import Context, Template
# '/' mean base no '/' mean add to current path, Django render function implicit 'templates/' no slash


# -------Homepage with Login---------
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)# Called User.Objects and Check db
        if user is not None:
            login(request, user)
            request.session['username'] = username
            request.session['is_teacher'] = user.profile.is_teacher
            request.session['id'] = user.id
            if user.profile.is_teacher == True:
                return redirect('/teacher/home')
                # return render(request,'teacher/teacher_homepage.html',{'user':user})
            else:
                return redirect('/student/home',{'user':user})
        else: 
            messages.warning(request, 'Failed Login')
            return HttpResponse('<h1>Failed Login </h1>')

    return render(request,'homepage/index.html')
# render(request, template_name, context=None, content_type=None, status=None, using=None)
# Combines a given template with a given context dictionary and returns an 
# HttpResponse object with that rendered text.

# -------- Register And Logout-------
def register(request):
    if request.method== 'POST':
        username = request.POST['username']
        if User.objects.filter(username=username):
            return HttpResponse('<h1>Username has already been taken.</h1>')
        
        school_id = request.POST['school_id']
        if len(school_id) < 8 or len(school_id) > 8:
            messages.warning(request, 'School id is 8 digit')
            return render(request,'homepage/error.html')
            
        if Profile.objects.filter(school_id=school_id):
            messages.warning(request, 'School id Already use')
            return render(request,'homepage/error.html')
            
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        password = request.POST['password']
        email = request.POST['email']
        
        user = User.objects.create_user(username=username,password=password,last_name=last_name
        , first_name=first_name,email=email)
        # rout to receiver in Model
        profile = Profile.objects.get(user=user)#.update(school_id=int(school_id))
        profile.school_id = int(school_id)
        #todo later reduce db query
        if int(school_id)%2 != 0:
            profile.is_student = True
            Student.objects.create(student_profile=profile,user=user)
        if int(school_id)%2 == 0:
            profile.is_student = True
            profile.is_teacher = True
            Teacher.objects.create(teacher_profile=profile,user=user)
        profile.save()
        messages.success(request, 'Registration is Sucessful. Please login.')
        return redirect('homepage')
    return render(request,'registration/register.html')