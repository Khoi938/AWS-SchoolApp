# Generated by Django 2.0.2 on 2018-07-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0008_auto_20180709_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address',
            new_name='street_address',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]