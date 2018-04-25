from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school_id = models.IntegerField()
    is_student = models.BooleanField('Student',default=False)
    is_teacher = models.BooleanField('Teacher',default=False)
    
class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    class1 = models.ForeignKey('Subject', null=True, on_delete = models.SET_NULL, related_name='class1')
    class2 = models.ForeignKey('Subject', null=True, on_delete = models.SET_NULL, related_name='class2')
    class3 = models.ForeignKey('Subject', null=True, on_delete = models.SET_NULL, related_name='class3')
    class3 = models.ForeignKey('Subject', null=True, on_delete = models.SET_NULL, related_name='class4')
    
class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teaches1 = models.ForeignKey('Subject', null=True, on_delete = models.SET_NULL, related_name='teaches1')
    teaches2 = models.ForeignKey('Subject', null=True, on_delete = models.SET_NULL, related_name='teaches2')
    teaches3 = models.ForeignKey('Subject', null=True, on_delete = models.SET_NULL, related_name='teaches3')
    teaches4 = models.ForeignKey('Subject', null=True, on_delete = models.SET_NULL, related_name='teaches4')
    
class Subject(models.Model):
    subject = models.CharField(max_length=30)
    monday = models.CharField(max_length=300)
    tuesday = models.CharField(max_length=300)
    wednesday = models.CharField(max_length=300)
    thursday = models.CharField(max_length=300)
    friday = models.CharField(max_length=300)
    
    