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
    class1 = models.ForeignKey('Algebra_101',blank=True, null=True, on_delete = models.SET_NULL, related_name='class1')
    class2 = models.ForeignKey('Biology_101',blank=True, null=True, on_delete = models.SET_NULL, related_name='class2')
    # class3 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='class3')
    # class3 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='class4')
    def __str__(self):
        return str(self.user.get_full_name()) #change to string
        
class Teacher(models.Model):
    teacher_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teaches1 = models.ForeignKey('Algebra_101',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches1')
    teaches2 = models.ForeignKey('Biology_101',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches2')
    # teaches3 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches3')
    # teaches4 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches4')
    def __str__(self):
        return str(self.user.get_full_name()) #change to string
        
# ---------------Classed Model----------------------
class Algebra_101(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete = models.CASCADE)
    weekly_agenda = models.CharField(max_length=450)
    
    monday_date = models.CharField(max_length=300)
    tuesday_date = models.CharField(max_length=300)
    wednesday_date = models.CharField(max_length=300)
    thursday_date = models.CharField(max_length=300)
    friday_date= models.CharField(max_length=300)
    
    monday_plan = models.CharField(max_length=300)
    tuesday_plan= models.CharField(max_length=300)
    wednesday_Plan= models.CharField(max_length=300)
    thursday_plan= models.CharField(max_length=300)
    friday_plan= models.CharField(max_length=300)
    def __str__(self):
        return 'Algebra 101 '+str(self.teacher)
        
class History_101(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete = models.CASCADE)
    weekly_agenda = models.CharField(max_length=450)
    
    def __str__(self):
        return 'History 101'

class Biology_101(models.Model):
    monday_date = models.CharField(max_length=300)
    tuesday_date = models.CharField(max_length=300)
    wednesday_date = models.CharField(max_length=300)
    thursday_date = models.CharField(max_length=300)
    friday_date= models.CharField(max_length=300)
    
    monday_plan = models.CharField(max_length=300)
    tuesday_plan= models.CharField(max_length=300)
    wednesday_Plan= models.CharField(max_length=300)
    thursday_plan= models.CharField(max_length=300)
    friday_plan= models.CharField(max_length=300)
    def __str__(self):
        return 'Algebra 101'
    

    
    