from django.contrib import admin
from .models import * #Profile, Student, Teacher, Algebra_101,Biology_101
# Register your models here.

admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Algebra_101)
admin.site.register(Biology_101)
