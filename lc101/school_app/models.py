from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    #username,first,last,email,password is extened from Django Auth User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    student_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # class1 = models.ForeignKey('Algebra_101',blank=True, null=True, on_delete = models.SET_NULL, related_name='class1')
    # class2 = models.ForeignKey('Biology_101',blank=True, null=True, on_delete = models.SET_NULL, related_name='class2')
    # class3 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='class3')
    # class3 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='class4')
    def __str__(self):
        return str(self.user.get_full_name()) #change to string
        
class Teacher(models.Model):
    teacher_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # teaches1 = models.ForeignKey('Algebra_101',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches1')
    # teaches2 = models.ForeignKey('Biology_101',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches2')
    teaches3 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches3')
    teaches4 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches4')
    def __str__(self):
        return str(self.user.get_full_name()) #change to string
        
# ---------------Classed Model----------------------
class Subject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    subject_name = models.CharField(max_length=150,default='')
    description = models.CharField(max_length=450,default='')
    
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
        return self.subject_name +' '+ str(self.teacher)+' '+self.description
        

        
class Classroom(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete = models.CASCADE)
    subject = models.OneToOneField(Teacher, on_delete = models.CASCADE)

@receiver(post_save, sender=Subject)
def create_classroom_object(sender, instance, created, **kwargs):
    if created:
        classroom = Classroom().objects.create(teacher=instance.teacher,subject=instance)
        classroom.save()
    
#     weekly_agenda = models.CharField(max_length=450,default='')
#     last_modifield = models.DateTimeField(auto_now_add=True, blank=True)
   
#     monday_date = models.DateField(default=None)
#     tuesday_date = models.DateField(default=None)
#     wednesday_date = models.DateField(default=None)
#     thursday_date = models.DateField(default=None)
#     friday_date= models.DateField(default=None)
    
#     monday_plan = models.CharField(max_length=300,default='a')
#     tuesday_plan= models.CharField(max_length=300,default='s')
#     wednesday_Plan= models.CharField(max_length=300,default='d')
#     thursday_plan= models.CharField(max_length=300,default='f')
#     friday_plan= models.CharField(max_length=300,default='g')
    
#     weekend_plan = models.CharField(max_length=300,default='h')
    

    
    