from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#------- Profile, Student, Teacher Model -------
class Profile(models.Model):
    #username,first,last,email,password is extened from Django Auth User
    user = models.OneToOneField(User, null=True, on_delete = models.SET_NULL)
    about = models.TextField(max_length=350, blank=True)
    address = models.CharField(max_length=200, blank=True)
    
    birth_date = models.DateField(null=True, blank=True)
    school_id = models.IntegerField(null=True, blank = True, default=0)
    
    is_student = models.BooleanField('Student', default=False)
    is_teacher = models.BooleanField('Teacher', default=False)
    def __str__(self):
        return self.user.get_full_name()
@receiver(post_save, sender=User)# Create a Profile when a User is create.
def create_profile_object(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
    
class Student(models.Model):
    profile = models.OneToOneField(Profile, null=True, on_delete = models.SET_NULL)
    user = models.OneToOneField(User, null=True, on_delete = models.SET_NULL)
    # Course_taking = models.ForeignKey('Course',blank=True, null=True, on_delete = models.SET_NULL, related_name='enrolled_Course')
    # classroom_taking = models.ManyToManyField('Classroom',blank=True)
    def __str__(self):
        return 'Student: ' + str(self.user.get_full_name()) #change to string
        
class Teacher(models.Model):
    profile = models.OneToOneField(Profile,null=True, on_delete = models.SET_NULL)
    user = models.OneToOneField(User, null=True, on_delete = models.SET_NULL)
    def __str__(self):
        return 'Teacher: ' + str(self.user.get_full_name()) #change to string
        
# --------------- Course, Classroom, Lesson Plan and Department's Model----------------------
class Course(models.Model): 
    course_number = models.CharField(max_length=20,default='12345678')
    abbreviated_title = models.CharField(max_length=150,default='')
    course_title = models.CharField(max_length=250,default='') #,unique=True)
    maximum_credit = models.CharField(max_length=10,default='')
    
    semester = models.CharField(max_length=50,default='')
    year = models.CharField(max_length=4,default='')
    teacher_name = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=450,default='')
    #Alert If  related name is use in ForeignKey, _set cannot be use! 
    teacher = models.ForeignKey('Teacher',blank=True, null=True, on_delete = models.SET_NULL, related_name='course_by_teacher')
    department = models.ForeignKey('Department',blank=True, null=True, on_delete = models.SET_NULL, related_name='belong_in_department')
    
    create_date = models.DateField(auto_now_add=True , blank=True,null=True,)
    #classroom = models.ForeignKey('Classroom', blank=True,null=True, on_delete = models.SET_NULL)
# A Course is bound to the teacher and create a classom upon creation. More room can be added later

class lesson_plan(models.Model):
    course_title = models.CharField(max_length=50,default='')
    teacher_idx = models.CharField(max_length=10,default='')
    create_date = models.DateField(auto_now_add=True, blank=True,null=True,)
    last_modifield = models.DateTimeField(auto_now=True, blank=True,null=True,)
   
    weekly_agenda = models.CharField(max_length=450,default='Agenda Goes Here')
    monday_date = models.DateField(blank=True, null=True)
    tuesday_date = models.DateField(blank=True, null=True)
    wednesday_date = models.DateField(blank=True, null=True)
    thursday_date = models.DateField(blank=True, null=True)
    friday_date= models.DateField(blank=True, null=True)
    
    monday_plan = models.CharField(max_length=400,default='a')
    tuesday_plan= models.CharField(max_length=400,default='s')
    wednesday_plan= models.CharField(max_length=400,default='d')
    thursday_plan= models.CharField(max_length=400,default='f')
    friday_plan= models.CharField(max_length=400,default='g')
    
    weekend_plan = models.CharField(max_length=300,default='h')
    
    teacher = models.ForeignKey('Teacher',blank=True, null=True, on_delete = models.SET_NULL, related_name='lesson_plan')
    
    def __str__(self):
        return 'Lesson plan for '+self.course_title +' Teacher: '+ str(self.teacher)

        
class Classroom(models.Model):
    course_title = models.CharField(max_length=50,default='')
    course_number = models.CharField(max_length=20,default='')
    teacher_name = models.CharField(max_length=50,default='')
    teacher_idx = models.CharField(max_length=10,default='')
    room_number = models.CharField(max_length=10,default='TBA')
    time = models.CharField(max_length=10,blank=True, null=True,default='TBA')
    description = models.CharField(max_length=300,default='TBA')
    # Use for statement to get value
    # Course = models.ManyToManyField(Course, blank=True)
    teacher = models.ForeignKey('Teacher',blank=True, null=True, on_delete = models.SET_NULL, related_name='classroom_by_teacher')
    course = models.ForeignKey('Course',blank=True, null=True, on_delete = models.SET_NULL, related_name='course_in_classroom')
    student = models.ManyToManyField(Student, blank=True)
    def __str__(self):
        return 'Course: ' + self.course_title +' Room #: '+self.room_number
@receiver(post_save, sender=Course)
def create_classroom_object(sender, instance, created, **kwargs):
    if created:
        classroom = Classroom.objects.create(course_title=instance.course_title,course_id=instance.id, teacher_name=instance.teacher_name,
        course=instance,teacher=instance.teacher)
# To Find the Classroom:
# teacher = Teacher.objects.filter(user=request.user)
# Course = Course.objects.filter(teacher_set=teacher, name ='Course_name')
# classroom = Classroom.objects.filter(teacher=teacher).filter(Course=Course)

        
class Department(models.Model):
    description = models.CharField(max_length=450,default='Department Description')
    name = models.CharField(max_length=75,default='', unique=True)
    
    # Course = models.ManyToManyField('Course',blank=True)
    teacher = models.ManyToManyField(Teacher,blank=True)
    student = models.ManyToManyField(Student,blank=True)
    
    def __str__(self):
        return 'LC High School ' + self.name + ' department.'
    

    
    