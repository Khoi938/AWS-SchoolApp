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
    school_id = models.IntegerField(default=0)
    
    is_student = models.BooleanField('Student', default=False)
    is_teacher = models.BooleanField('Teacher', default=False)
    def __str__(self):#Return the string representation of the object
        return '%s %s'%(self.user.first_name, self.user.last_name)
@receiver(post_save, sender=User)
def create_profile_object(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()
    
        
class Student(models.Model):
    student_profile = models.OneToOneField(Profile, null=True, on_delete = models.SET_NULL)
    user = models.OneToOneField(User, null=True, on_delete = models.SET_NULL)
    # class1 = models.ForeignKey('Algebra_101',blank=True, null=True, on_delete = models.SET_NULL, related_name='class1')
    # class2 = models.ForeignKey('Biology_101',blank=True, null=True, on_delete = models.SET_NULL, related_name='class2')
    # class3 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='class3')
    # class3 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='class4')
    def __str__(self):
        return str(self.user.get_full_name()) #change to string
        
class Teacher(models.Model):
    teacher_profile = models.OneToOneField(Profile,null=True, on_delete = models.SET_NULL)
    user = models.OneToOneField(User, null=True, on_delete = models.SET_NULL)
    # teaches1 = models.ForeignKey('Algebra_101',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches1')
    # teaches2 = models.ForeignKey('Biology_101',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches2')
    teaches = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches')
    # teaches4 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches4')
    def __str__(self):
        return str(self.user.get_full_name()) #change to string
        
# --------------- Subject, Classroom, Department's Model----------------------
class Subject(models.Model):
    teacher = models.ManyToManyField(Teacher)
    name = models.CharField(max_length=150,default='')
    description = models.CharField(max_length=450,default='')
    classroom = models.ForeignKey('Classroom', blank=True,null=True, on_delete = models.SET_NULL)
    
    weekly_agenda = models.CharField(max_length=450,default='Agenda Goes Here')
    last_modifield = models.DateTimeField(auto_now_add=True, blank=True)
   
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
    
    def __str__(self):
        return self.name +' '+ str(self.teacher)+' '+self.description

        
class Classroom(models.Model):
    description = models.CharField(max_length=450,default='')
    name = models.CharField(max_length=50,default='')
    
    semester = models.CharField(max_length=50,default='')
    room_number = models.CharField(max_length=50,default='')
    year = models.CharField(max_length=5,default='')
    
    teacher = models.OneToOneField(Teacher, null=True, on_delete = models.SET_NULL)
    subject = models.ManyToManyField(Subject, blank=True)
    student = models.ManyToManyField(Student, blank=True)
    def __str__(self):
        return 'Subject: ' + self.subject.name + self.description
@receiver(post_save, sender=Subject)
def create_classroom_object(sender, instance, created, **kwargs):
    if created:
        classroom = Classroom.objects.create(teacher=instance.teacher,subject=instance)
        classroom.save()
        
class Department(models.Model):
    description = models.CharField(max_length=450,default='Department Description')
    name = models.CharField(max_length=75,default='Department Name')
    
    subject = models.ManyToManyField(Subject,blank=True)
    teacher = models.ManyToManyField(Teacher,blank=True)
    student = models.ManyToManyField(Student,blank=True)
    
    def __str__(self):
        return 'LC High School ' + self.name + ' department.'
    

    
    