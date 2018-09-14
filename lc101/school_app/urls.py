# from same folder import views
from . import views, views_logged
from django.urls import path
from django.contrib.auth import views as auth_login_test

urlpatterns=[
    path('',views.index, name = 'index'),
    path('test_page_2',views.test_page_2,name='test_page_2'),
    path('learning_JS',views.learning_JS, name='learning_JS'),
    path('homepage',views.index, name = 'homepage'),
    path('register',views.register, name='register'),
    path('account_management/',views.account_management, name='account_management'),
    
    path('account_management/<str:modify>',views.account_management_edit,name='account_management_edit'),
    path('account_management_save/',views.account_management_save,name='account_management_save'),
    
    #when user visit this address, call this function
    path('teacher',views_logged.teacher, name='teacher'),
    path('teacher/<int:sort>/',views_logged.teacher, name='teacher_sort'),
    # path('teacher/home',views_logged.teacher, name='teacher_home'),
    
    path('teacher/add_course',views_logged.add_course, name='add_course'),
    path('teacher/edit_course', views_logged.edit_course, name='edit_course'),
    path('teacher/edit_course/<int:course_id>/', views_logged.edit_course, name='edit_course'),
    path('teacher/drop_course', views_logged.drop_course, name='drop_course'),
    path('teacher/archive_course', views_logged.archive_course, name='archive_course'),
    
    
    # path('teacher/lesson_plan',views_logged.lesson_plan, name='lesson_plan'),
    path('teacher/lesson_plan/<int:course_id>/',views_logged.lesson_plan, name='view_lesson_plan'),
    path('teacher/lesson_plan/weekly_lesson_plan/<int:lesson_plan_id>',views_logged.weekly_lesson_plan, name='weekly_lesson_plan'),
    path('teacher/lesson_plan/update_lesson_plan/',views_logged.edit_lesson_plan, name='update_lesson_plan'),
    path('teacher/lesson_plan/edit_lesson_plan/<int:lesson_plan_id>',views_logged.edit_lesson_plan, name='edit_lesson_plan'),
    path('teacher/lesson_plan/delete_lesson_plan/<int:course_id>/<int:lesson_plan_id>',views_logged.edit_lesson_plan, name='delete_lesson_plan'),
    path('teacher/lesson_plan/delete_lesson_plan/',views_logged.delete_lesson_plan, name='delete_lesson_plan'),
    
    path('teacher/lesson_plan/add/',views_logged.add_lesson_plan, name='save_lesson_plan'),#save newly created lesson_plan
    path('teacher/lesson_plan/add/<int:course_id>/',views_logged.add_lesson_plan, name='add_lesson_plan'),
    # path('teacher/edit_lesson_plan/<int:course_id>/<int:plan_id>/',views_logged.lesson_plan, name='view_lesson_plan'),
   
    path('teacher/classroom/add_classroom', views_logged.add_classroom, name='add_classroom'),
    path('teacher/classroom/add_classroom/<int:course_id>', views_logged.add_classroom, name='add_classroom'),
   
    path('teacher/classroom', views_logged.classroom, name='classroom_list'),
    path('teacher/classroom/<int:course_id>', views_logged.classroom, name='classroom_view'),
    
    path('teacher/classroom/edit_classroom/', views_logged.edit_classroom, name='save_edit_classroom'),
    path('teacher/classroom/edit_classroom/<int:classroom_id>', views_logged.edit_classroom, name='edit_classroom'),
    path('teacher/classroom/edit_classroom/<int:classroom_id>/<str:rout_from>', views_logged.edit_classroom, name='edit_classroom'),
    
    path('teacher/classroom/detached_classroom/', views_logged.detached_classroom, name='detached_classroom'),
    path('teacher/classroom/schedule_conflict/', views_logged.schedule_conflict, name='schedule_conflict'),
    
   
    # path('teacher/classroom/detached_classroom/<int:classroom_id>', views_logged.detached_classroom, name='detached_classroom'),
    
    path('teacher/student_list', views_logged.student_list, name='student_list'),
    path('teacher/student_views', views_logged.student_views, name='student_views'),
    path('teacher/student_views/<int:student_id>/', views_logged.student_views, name='student_views'),
    
    path('student',views_logged.student,name='student'),
    path('student/home',views_logged.student,name='student_home'),
    
    path('home_redirect',views_logged.home_redirect, name = 'home_redirect'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout')]