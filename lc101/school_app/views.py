from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from school_app.models import Profile, Student, Teacher
# from school_app.models_views import user_views
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
        else: return HttpResponse('<h1>Failed login</h1>')

        
        
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
        if Profile.objects.filter(school_id=school_id):
            return HttpResponse('<h1>Invalid School ID</h1>')
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
        return HttpResponse('<h1>SUcess</h1>')
    return render(request,'registration/register.html')