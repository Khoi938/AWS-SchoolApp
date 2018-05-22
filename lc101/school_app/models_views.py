# from django.db import models
# from django.contrib.auth.models import User
# from school_app.models import Profile, Student, Teacher
# # from django.db.models.signals import post_save
# # from django.dispatch import receiver

# class User_views(User):
#     username = User.username
#     first_name = User.first_name
#     last_name = User.last_name
#     profile = Profile.objects.filter(user = User)
#     about = profile.about
#     def full_name(self):
#         return '%s %s'%(self.first_name, self.last_name)
#     def __str__(self):
#         return '%s %s'%(self.first_name, self.last_name)
    