# Generated by Django 2.0.2 on 2018-06-11 10:56

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
                ('room_number', models.CharField(default='24', max_length=10)),
                ('subject_name', models.CharField(default='', max_length=50)),
                ('teacher_name', models.CharField(default='', max_length=50)),
                ('time', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='Department Description', max_length=450)),
                ('name', models.CharField(default='Department Name', max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, max_length=350)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('school_id', models.IntegerField(blank=True, default=0, null=True)),
                ('is_student', models.BooleanField(default=False, verbose_name='Student')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='Teacher')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_app.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('description', models.CharField(default='', max_length=450)),
                ('teacher_name', models.CharField(default='', max_length=50)),
                ('semester', models.CharField(default='', max_length=50)),
                ('year', models.CharField(default='', max_length=4)),
                ('weekly_agenda', models.CharField(default='Agenda Goes Here', max_length=450)),
                ('last_modifield', models.DateTimeField(auto_now_add=True)),
                ('monday_date', models.DateField(blank=True, null=True)),
                ('tuesday_date', models.DateField(blank=True, null=True)),
                ('wednesday_date', models.DateField(blank=True, null=True)),
                ('thursday_date', models.DateField(blank=True, null=True)),
                ('friday_date', models.DateField(blank=True, null=True)),
                ('monday_plan', models.CharField(default='a', max_length=400)),
                ('tuesday_plan', models.CharField(default='s', max_length=400)),
                ('wednesday_plan', models.CharField(default='d', max_length=400)),
                ('thursday_plan', models.CharField(default='f', max_length=400)),
                ('friday_plan', models.CharField(default='g', max_length=400)),
                ('weekend_plan', models.CharField(default='h', max_length=300)),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_app.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='in_room', to='school_app.Classroom')),
                ('profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school_app.Profile')),
                ('teaches', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teaches_subject', to='school_app.Subject')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='subject_taking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enrolled_subject', to='school_app.Subject'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='department',
            name='student',
            field=models.ManyToManyField(blank=True, to='school_app.Student'),
        ),
        migrations.AddField(
            model_name='department',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_subject', to='school_app.Subject'),
        ),
        migrations.AddField(
            model_name='department',
            name='teacher',
            field=models.ManyToManyField(blank=True, to='school_app.Teacher'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='student',
            field=models.ManyToManyField(blank=True, to='school_app.Student'),
        ),
    ]
