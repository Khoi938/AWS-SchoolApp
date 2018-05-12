# Generated by Django 2.0.2 on 2018-05-10 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0004_auto_20180507_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biology_101',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday_date', models.CharField(max_length=300)),
                ('tuesday_date', models.CharField(max_length=300)),
                ('wednesday_date', models.CharField(max_length=300)),
                ('thursday_date', models.CharField(max_length=300)),
                ('friday_date', models.CharField(max_length=300)),
                ('monday_plan', models.CharField(max_length=300)),
                ('tuesday_plan', models.CharField(max_length=300)),
                ('wednesday_Plan', models.CharField(max_length=300)),
                ('thursday_plan', models.CharField(max_length=300)),
                ('friday_plan', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, max_length=500)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('school_id', models.IntegerField(default=0)),
                ('email', models.CharField(default='None', max_length=100)),
                ('is_student', models.BooleanField(default=False, verbose_name='Student')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='Teacher')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='class3',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='teaches3',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='teaches4',
        ),
        migrations.AlterField(
            model_name='student',
            name='class2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class2', to='homepage.Biology_101'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='homepage.Profile'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='homepage.Profile'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teaches2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teaches2', to='homepage.Biology_101'),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
