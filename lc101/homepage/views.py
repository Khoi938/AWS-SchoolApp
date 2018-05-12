from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from homepage.models import Profile, Student, Teacher
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        
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
        if User.objects.filter(school_id=school_id):
            return HttpResponse('<h1>Invalid School ID</h1>')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        
        password = request.POST['password']
        email = request.POST['email']
        
        is_teacher = False
        user = User.objects.create_user(username=username,password=password,last_name=last_name
        , first_name=first_name,email=email)
        
        if int(school_id)%2!=0:
            user.Profile.is_student = False
            Student.objects.create(student=user)
        if int(school_id)%1==0:
            Teacher.objects.create(teacher=user)
        return HttpResponse('<h1>SUcess</h1>')
    return render(request,'homepage/register.html')