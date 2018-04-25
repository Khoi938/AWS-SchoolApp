from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school_id = models.IntegerField(max_length=10)
    is_student = models.BooleanField('Student',default=False)
    is_teacher = models.BooleanField('Teacher',default=False)
    
class Math():
    monday = models.CharField(max_length=300)
    Tuesday = models.CharField(max_length=300)
    monday = models.CharField(max_length=300)
    monday = models.CharField(max_length=300)
    monday = models.CharField(max_length=300)
    