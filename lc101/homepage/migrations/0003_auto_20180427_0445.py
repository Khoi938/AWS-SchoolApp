# Generated by Django 2.0.2 on 2018-04-27 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20180427_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='homepage.User'),
        ),
    ]
