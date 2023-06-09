# Generated by Django 4.1.8 on 2023-04-21 04:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarkMeApp', '0008_instructors_attendance_id_students_attendance_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date_signed',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 5, 50, 11, 9161)),
        ),
        migrations.AlterField(
            model_name='courses',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 5, 50, 11, 7184)),
        ),
        migrations.AlterField(
            model_name='institutions',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 5, 50, 11, 8183)),
        ),
        migrations.AlterField(
            model_name='institutions',
            name='name',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='instructors',
            name='attendance_id',
            field=models.CharField(default='I1-4jg', max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='attendance_id',
            field=models.CharField(default='yEZ3Tg', max_length=10),
        ),
    ]
