from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from school_app.models import *
from django.contrib import messages
from django.contrib.auth import authenticate
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = user.username
            if user.profile.is_teacher == True:
                return render(request,'teacher/teacher_homepage.html',{'user':user})
            else:
                return render(request,'student/student_homepage.html')
        else: 
            messages.warning(request, 'Failed Login')
            return render(request,'homepage/error.html')

    return render(request,'homepage/index.html')
# render(request, template_name, context=None, content_type=None, status=None, using=None)
# Combines a given template with a given context dictionary and returns an 
# HttpResponse object with that rendered text.


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