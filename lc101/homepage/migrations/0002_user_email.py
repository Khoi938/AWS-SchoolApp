# Generated by Django 2.0.2 on 2018-05-01 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
