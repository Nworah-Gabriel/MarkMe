# Generated by Django 4.1.8 on 2023-04-25 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarkMeApp', '0028_attendance_instructor_attendance_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date_signed',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 25, 14, 11, 56, 847357)),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_id',
            field=models.CharField(default='lKt0f1FZUEY', max_length=50),
        ),
        migrations.AlterField(
            model_name='courses',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 25, 14, 11, 56, 846358)),
        ),
        migrations.AlterField(
            model_name='institutions',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 25, 14, 11, 56, 847357)),
        ),
        migrations.AlterField(
            model_name='instructors',
            name='attendance_id',
            field=models.CharField(default='ZfejoA', max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='attendance_id',
            field=models.CharField(default='lafcww', max_length=50),
        ),
    ]
