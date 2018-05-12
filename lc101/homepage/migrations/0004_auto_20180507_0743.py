# Generated by Django 2.0.2 on 2018-05-07 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20180501_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algebra_101',
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
        migrations.AlterField(
            model_name='student',
            name='class1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class1', to='homepage.Algebra_101'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teaches1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teaches1', to='homepage.Algebra_101'),
        ),
    ]
