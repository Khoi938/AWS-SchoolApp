# Generated by Django 2.0.2 on 2018-08-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]