# Generated by Django 2.0.2 on 2018-06-22 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0002_auto_20180617_0651'),
    ]

    operations = [
        migrations.CreateModel(
            name='lesson_plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(default='', max_length=50)),
                ('teacher_idx', models.CharField(default='', max_length=10)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
                ('last_modifield', models.DateTimeField(auto_now=True, null=True)),
                ('weekly_agenda', models.CharField(default='Agenda Goes Here', max_length=450)),
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
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson_plan', to='school_app.Teacher')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='friday_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='friday_plan',
        ),
        migrations.RemoveField(
            model_name='course',
            name='last_modifield',
        ),
        migrations.RemoveField(
            model_name='course',
            name='monday_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='monday_plan',
        ),
        migrations.RemoveField(
            model_name='course',
            name='thursday_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='thursday_plan',
        ),
        migrations.RemoveField(
            model_name='course',
            name='tuesday_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='tuesday_plan',
        ),
        migrations.RemoveField(
            model_name='course',
            name='wednesday_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='wednesday_plan',
        ),
        migrations.RemoveField(
            model_name='course',
            name='weekend_plan',
        ),
        migrations.RemoveField(
            model_name='course',
            name='weekly_agenda',
        ),
        migrations.AddField(
            model_name='classroom',
            name='course_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='classroom',
            name='teacher_idx',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
