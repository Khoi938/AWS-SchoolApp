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
    return render(request,'teacher/teacher_homepage.html')
    # teacher = Teacher.objects.get(user=request.user)
    # Course = teacher.course_by_teacher.all()
    # return render(request,'teacher/teacher_homepage.html',{'teacher':teacher,'Course':Course})
    
def add_course(request):
    if is_login(request) == True:
        if request.user.profile.is_teacher == False:
            messages.warning(request, "You don't have Instructor's Privilege!")
            return redirect('/')
        elif request.method == 'POST':
    
            if request.POST['year'].isnumeric(): # Check year for integer
                year = request.POST['year']
            else:
                return redirect('/teacher/add_course')
            
            semester = request.POST['semester']
            subject_description = request.POST['description']
            department_course = request.POST['department_course']
            
            split_dict = department_course.split('|')
            department_name = split_dict[0]  # Break Department away from Course 
            course_title = split_dict[1]
            
            if Department.objects.filter(name=department_name).first() == None: # If Department not found, Create one
                department = Department.objects.create(name=department_name)
            department = Department.objects.filter(name=department_name).first()
            
            new_course = Course.objects.create(course_title=course_title, description=subject_description, 
            teacher_name=request.user.get_full_name(),teacher=request.user.teacher,
            semester=semester, year=year, department=department)# Rout to receiver to create Classroom mode
            
            classroom = Classroom.objects.filter(course=new_course).first()
            classroom.semester = semester
            classroom.year = year
            classroom.save()
            
            messages.success(request, 'Course: '+ new_course.course_title+', Department: '+ department.name+', Instructor: '+ 
            request.user.get_full_name()+ ' has been created.' )
            return redirect('/teacher/add_course')
            # return render(request,'teacher/add_course.html')
        else:
            return render(request,'teacher/add_course.html')
            

def edit_course(request,course_id=None):
    if is_login(request) == True:
        if request.user.profile.is_teacher == False:
            messages.warning(request, "You don't have Instructor's Privilege!")
            return redirect('/')
        if request.method == 'POST':# and class_id==None:
            monday_date = request.POST['monday_date']
            monday_plan = request.POST['monday_plan']
            course_id = request.POST['course_id']
            course = Course.objects.filter(id=course_id).first()
            course.monday_date = monday_date
            course.monday_plan = monday_plan
            course.save()
            messages.success(request, course.course_title + ' have been updated.')
            return redirect('/teacher')
        else:
            edit_course=Course.objects.filter(id=class_id)
            return render(request,'teacher/edit_course.html',{'edit_course':edit_course})

def classroom(request,course_id=None):
    if is_login(request) == True:
        if request.user.profile.is_teacher == False:
            messages.warning(request, "You don't have Instructor's Privilege!")
            return redirect('/')
        course = Course.objects.filter(id=course_id).first()
        classes = Classroom.objects.filter(course=course)
        return render(request,'teacher/classroom/classroom_list_by_course.html',
        {'classes':classes,'course':course})
        
def add_classroom(request,course_id=None):
    if is_login(request) == True:
        if request.user.profile.is_teacher == False:
            messages.warning(request, "You don't have Instructor's Privilege!")
            return redirect('/')
        course = Course.objects.filter(id=course_id).first()
        return render(request,'teacher/classroom/add_classroom.html',
        {'course':course})
    
        
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

