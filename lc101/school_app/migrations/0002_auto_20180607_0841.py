# Generated by Django 2.0.2 on 2018-06-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='wednesday_Plan',
            new_name='wednesday_plan',
        ),
        migrations.AddField(
            model_name='subject',
            name='friday_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='thursday_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='tuesday_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='wednesday_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='weekly_agenda',
            field=models.CharField(default='Agenda Goes Here', max_length=450),
        ),
    ]
