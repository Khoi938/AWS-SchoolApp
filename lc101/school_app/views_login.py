from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from school_app.models import Profile, Student, Teacher
from django.contrib.auth import authenticate

def teacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return render(request,'teacher/teacher_homepage.html')
        else: return HttpResponse('<h1>Failed login</h1>')
    return HttpResponse('<h1>Failed login</h1>') #render(request,'teacher/teacher_homepage.html')
