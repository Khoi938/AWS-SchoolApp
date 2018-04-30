from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    school_id = models.IntegerField()
    is_student = models.BooleanField('Student',default=False)
    is_teacher = models.BooleanField('Teacher',default=False)
    def __str__(self):#Return the string representation of the object
        return '%s %s'%(self.first_name,self.last_name)
        
class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    class1 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='class1')
    class2 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='class2')
    class3 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='class3')
    class3 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='class4')
    def __str__(self):
        return str(self.student) #change to string
        
class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teaches1 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches1')
    teaches2 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches2')
    teaches3 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches3')
    teaches4 = models.ForeignKey('Subject',blank=True, null=True, on_delete = models.SET_NULL, related_name='teaches4')
    
class Subject(models.Model):
    subject = models.CharField(max_length=30)
    monday = models.CharField(max_length=300)
    tuesday = models.CharField(max_length=300)
    wednesday = models.CharField(max_length=300)
    thursday = models.CharField(max_length=300)
    friday = models.CharField(max_length=300)
    
    