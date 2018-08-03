# Generated by Django 2.0.2 on 2018-08-03 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(default='', max_length=50)),
                ('course_number', models.CharField(default='', max_length=20)),
                ('teacher_name', models.CharField(default='', max_length=50)),
                ('teacher_idx', models.CharField(default='', max_length=10)),
                ('room_number', models.CharField(default='TBA', max_length=10)),
                ('time', models.TimeField(default='00:00')),
                ('description', models.CharField(default='TBA', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(default='12345678', max_length=20)),
                ('abbreviated_title', models.CharField(default='', max_length=150)),
                ('course_title', models.CharField(default='', max_length=250)),
                ('maximum_credit', models.CharField(default='', max_length=10)),
                ('semester', models.CharField(default='', max_length=50)),
                ('year', models.CharField(default='', max_length=4)),
                ('teacher_name', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=450)),
                ('is_archive', models.BooleanField(default=False)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='Department Description', max_length=450)),
                ('name', models.CharField(default='', max_length=75, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson_plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(default='', max_length=50)),
                ('teacher_idx', models.CharField(default='', max_length=10)),
                ('week_number', models.CharField(default='', max_length=10)),
                ('agenda', models.CharField(default='Agenda Goes Here', max_length=450)),
                ('monday_date', models.DateField(blank=True, null=True)),
                ('tuesday_date', models.DateField(blank=True, null=True)),
                ('wednesday_date', models.DateField(blank=True, null=True)),
                ('thursday_date', models.DateField(blank=True, null=True)),
                ('friday_date', models.DateField(blank=True, null=True)),
                ('monday_assignment', models.CharField(default='a', max_length=400)),
                ('tuesday_assignment', models.CharField(default='s', max_length=400)),
                ('wednesday_assignment', models.CharField(default='d', max_length=400)),
                ('thursday_assignment', models.CharField(default='f', max_length=400)),
                ('friday_assignment', models.CharField(default='g', max_length=400)),
                ('weekend_assignment', models.CharField(default='h', max_length=300)),
                ('last_modifield', models.DateTimeField(auto_now=True, null=True)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_app.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zip_code', models.CharField(blank=True, max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('emergency_contact', models.CharField(blank=True, max_length=20)),
                ('relationship', models.CharField(blank=True, max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('school_id', models.CharField(blank=True, default=0, max_length=15, null=True)),
                ('is_student', models.BooleanField(default=False, verbose_name='Student')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='Teacher')),
                ('about', models.TextField(blank=True, max_length=300)),
                ('hobby', models.TextField(blank=True, max_length=100)),
                ('favorite_food', models.TextField(blank=True, max_length=100)),
                ('favorite_subject', models.TextField(blank=True, max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_app.Profile')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_app.Profile')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lesson_plan',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_app.Teacher'),
        ),
        migrations.AddField(
            model_name='department',
            name='student',
            field=models.ManyToManyField(blank=True, to='school_app.Student'),
        ),
        migrations.AddField(
            model_name='department',
            name='teacher',
            field=models.ManyToManyField(blank=True, to='school_app.Teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='belong_in_department', to='school_app.Department'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_by_teacher', to='school_app.Teacher'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_in_classroom', to='school_app.Course'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='student',
            field=models.ManyToManyField(blank=True, to='school_app.Student'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classroom_by_teacher', to='school_app.Teacher'),
        ),
    ]
