from django.shortcuts import render, redirect
from django.http import HttpResponse

from school_app.models import *
from school_app.views_functions import *
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.template import Context, Template

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views.decorators.http import require_http_methods

# '/' mean base no '/' mean add to current path, Django render function implicit locate 'templates/'



# -------Homepage with Login---------
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)# Called User.Objects and Check db
        if user is not None:
            auth_login(request, user)
            if user.profile.is_teacher == True:
                return redirect('/teacher')
                
            else:
                return redirect('/student/home',{'user':user})
        else: 
            messages.warning(request, 'Failed Login')
            return HttpResponse('<h1>Failed Login </h1>')

    return render(request,'homepage/index.html')
# render(request, template_name, context=None, content_type=None, status=None, using=None)
# Combines a given template with a given context dictionary and returns an 
# HttpResponse object with that rendered text.

# -------- Register, Login, Logout -------
def register(request):
    if request.method== 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        email = request.POST['email']
        school_id = request.POST['school_id']
        
        input_dict = {'username':username, 'first_name':first_name, 'last_name':last_name, 
        'email':email,'school_id':school_id}
        
        if User.objects.filter(username=username):
            messages.warning(request, 'Username has already been taken.')
            return render(request,'registration/register.html',{'input_dict':input_dict})
        
        if school_id.isdigit() == False: # Check to see if str can be integer
            messages.warning(request, 'School id is an 8 digit number.')
            return render(request,'registration/register.html',{'input_dict':input_dict})
            
        if len(school_id) < 8 or len(school_id) > 8:
            messages.warning(request, 'School id is an 8 digit number.')
            return render(request,'registration/register.html',{'input_dict':input_dict})
            
        if Profile.objects.filter(school_id=school_id):
            messages.warning(request, 'School id is Already in use.')
            return render(request,'registration/register.html',{'input_dict':input_dict})
        
        user = User.objects.create_user(username=username,password=password,last_name=last_name
        ,first_name=first_name,email=email)# At this point receiver in models.py is called
        
        profile = Profile.objects.get(user=user)#.update(school_id=int(school_id))
        profile.school_id = int(school_id) #todo later reduce db query
        
        if int(school_id)%2 != 0:
            profile.is_student = True
            Student.objects.create(profile=profile,user=user)
        if int(school_id)%2 == 0:
            profile.is_teacher = True
            Teacher.objects.create(profile=profile,user=user)
        profile.save()
        messages.success(request, 'Registration is Sucessful. Please login.')
        return redirect('homepage')
    return render(request,'registration/register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.profile.is_teacher == True:
                return redirect('/teacher/home')
            else:
                return redirect('/student/home')
        
        elif User.objects.filter(username=username).first() == None:
            messages.warning(request, 'Username not found.')
            return render(request,'registration/login.html')
        
        elif User.objects.filter(password=password).first() == None:
            messages.warning(request, 'Incorrect password.')
            return render(request,'registration/login.html') 
    
    return render(request,'registration/login.html')

def logout(request):
    if is_login(request) == False: 
        return redirect('/homepage')
    username = request.user.username #request.user.get_full_name()
    messages.success(request, username + ' Sucessfully logged out.')
    auth_logout(request)
    return redirect('/')   

#------ Account Management and Profiles Views/Edit -----

def account_management(request):
    if is_login(request) == False: 
        return redirect('/login')
    if request.method == 'POST':
        return None
    
    return render(request,'account_profile/view_account.html')
    
def account_management_edit(request,modify=None):
    if is_login(request) == False: 
        return redirect('/login')
    if modify == 'address':
        return render(request,'account_profile/edit_profile/edit_address.html')
    if modify == 'email':
        return render(request,'account_profile/edit_profile/edit_email.html')
    if modify == 'phone_number':
        return render(request,'account_pofile/edit_profile/edit_phone_number.html')
    if modify == 'emergency_contact':
        return render(request,'account_profile/edit_profile/edit_emergency_contact.html')
    
    