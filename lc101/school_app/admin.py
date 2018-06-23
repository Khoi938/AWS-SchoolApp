from django.contrib import admin
from .models import * #Profile, Student, Teacher, Subject
# Register your models here.

admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Classroom)
admin.site.register(Department)
admin.site.register(Lesson_plan)
