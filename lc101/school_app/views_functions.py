from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from school_app.models import *
# ----- Custom Functions goes Here -----

# Check to see if user is login add message
def is_login(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login or Create an Account.")
        return False
    return True
    
# Check to see if a User is a Teacher
def is_teacher(request): 
    if request.user.profile.is_teacher == False:
        messages.warning(request, "You don't have Instructor's Privilege!")
        return False
    return True

# Add Class to Student and Check number of current class
def add_class(request, student, subject):
        if student.enrolled.count() >= 7:#Count hit DB return with num, len(s) pull the entire list out and count it.
            messages.warning(request,'Student cannot be enrolled in more than 7 Class')
            return False
        else:
            student.enrolled.add(subject)
            return 
# Use to check radio input text field for custom entry
def other_check(post,custom):
    if post == 'other' or post == 'Other':
        return custom
    else: 
        return post
    
# Sort order in Teacher homepage Course List 
def sort_order(x):
    if x == 1:
        return 'years'
# Check to see if classroom have the same time in the same semester/year
# WHY WONT YOU WORK!!!
def schedule_conflict(course_sorted):
    classroom = Classroom.objects.filter(course__in=course_sorted).exclude(time__isnull=True)
    # can chain multiple exclude and filter, if multiple arg mean have all, if chain meaning need only one.
    time=[]
    time_conflict=[]
    schedule_conflict=[]
    first_room_added=[]
    for room in classroom:
        if room.time not in time:
            time.append(room.time)
            first_room_added.append(room)
        else:
            time_conflict.append(room)
    for room in first_room_added:
        for room2 in time_conflict:
            if room.time == room2.time and room.semester == room2.semester and room.year==room2.year:
                time_conflict.append(room)
                # insert(0,room)
                break
    for room in time_conflict:
        count = 0
        for room2 in time_conflict:
            if room.time == room2.time and room.semester == room2.semester and room.year == room2.year:
                count += 1
        if count >=2:
            schedule_conflict.append(room)
    sorted_schedule_conflict = sorted(schedule_conflict,key=attrgetter('year','semester','course_title',))
    return sorted_schedule_conflict
      