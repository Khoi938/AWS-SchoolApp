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
    
            if request.POST['year'].isnumeric(): # Check year for integer
                year = request.POST['year']
            else:
                return redirect('/teacher/add_class')
                
            department_subject = request.POST['department_subject']
            split_dict = department_subject.split('|')
            department_name = split_dict[0]  # Break Department away from Subject 
            subject_name = split_dict[1]
            
            if Department.objects.filter(name=department_name).first() == None:
                department = Department.objects.create(name=department_name)
            else:     # If Department not found, Create one
                department = Department.objects.filter(name=department_name).first
            
            semester = request.POST['semester']
            subject_description = request.POST['description']
            
    
            teacher_id = request.user.teacher.id
            teacher = Teacher.objects.filter(id=teacher_id).first()
            
            new_subject = Subject.objects.create(teacher=teacher,name=subject_name, description=subject_description)
            
            department.subject.add(new_subject)
            classroom = Classroom.objects.filter(subject=new_subject).first()
            classroom.semester = semester
            classroom.year = year
            classroom.save()
            
            messages.success(request, new_subject.subject_name+' Department: '+ department.name+' Instructor: '+ 
            request.user.get_full_name()+ ' has been created.' )
            
            return render(request,'teacher/add_class.html')
        else:
            return render(request,'teacher/add_class.html')
            

def edit_class(request,class_id=None):
    if is_login(request) == True:
        if request.user.profile.is_teacher == False:
            messages.warning(request, "You don't have Instructor's Privilege!")
            return redirect('/')
        if request.method == 'POST':# and class_id==None:
            monday_date = request.POST['monday_date']
            monday_plan = request.POST['monday_plan']
            subject_id = request.POST['subject_id']
            subject = Subject.objects.filter(id=subject_id).first()
            subject.monday_date = monday_date
            subject.monday_plan = monday_plan
            subject.save()
            messages.success(request, subject.subject_name + ' have been updated.')
            return redirect('/teacher')
        else:
            edit_class=Subject.objects.filter(id=class_id)
            return render(request,'teacher/edit_class.html',{'edit_class':edit_class})

def student_list(request):
    if is_login(request) == True:
        if request.user.profile.is_teacher == False:
            messages.warning(request, "You don't have Instructor's Privilege!")
            return redirect('/')
        else:
            students=Student.objects.all()
            return render(request,'teacher/student_list.html',{'students':students})

def student_views(request,student_id=None):
    if is_login(request) == True:
        if request.user.profile.is_teacher == False:
            messages.warning(request, "You don't have Instructor's Privilege!")
            return redirect('/')
        if request.method == 'POST':
            classroom_id = request.POST['classroom_id']
            student_id = request.POST['student_id']
            classroom = Classroom.objects.filter(id=classroom_id).first()
            user = User.objects.filter(id=student_id).first()
            student = Student.objects.filter(user=user).first()
            classroom.student.add(student)
            return redirect('/teacher/student_list')
        if student_id != None:
            user = User.objects.filter(id=student_id).first() #refactor later to reduce db query
            student = Student.objects.filter(user=user).first()
            classroom = Classroom.objects.filter(student=student)
            student = Student.objects.filter(user=user)
            all_classroom = Classroom.objects.all()
            return render(request,'teacher/student_class_edit.html',
            {'classroom':classroom,'students':student,'all_classroom':all_classroom})
        else:
            students=Student.objects.all()
            return render(request,'teacher/student_list.html',{'students':students})
          

            
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
    full_name = request.user.username #request.user.get_full_name()
    messages.success(request, full_name + ' have logged out.')
    auth_logout(request)
    return redirect('/') 

#----- Redirect User to homepage according to status -----
def home_redirect(request):
    login_check(request)
    if request.user.profile.is_teacher == True:
        return redirect('/teacher')
    else:
        return redirect('/student')

