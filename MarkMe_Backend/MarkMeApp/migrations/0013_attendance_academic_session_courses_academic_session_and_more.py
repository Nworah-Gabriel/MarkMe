# Generated by Django 4.1.8 on 2023-04-21 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarkMeApp', '0012_alter_attendance_date_signed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='academic_session',
            field=models.CharField(default=datetime.datetime(2023, 4, 21, 8, 2, 57, 399868), max_length=20),
        ),
        migrations.AddField(
            model_name='courses',
            name='academic_session',
            field=models.CharField(default=datetime.datetime(2023, 4, 21, 8, 2, 57, 398868), max_length=20),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date_signed',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 8, 2, 57, 399868)),
        ),
        migrations.AlterField(
            model_name='courses',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 8, 2, 57, 398868)),
        ),
        migrations.AlterField(
            model_name='institutions',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 21, 8, 2, 57, 398868)),
        ),
        migrations.AlterField(
            model_name='instructors',
            name='attendance_id',
            field=models.CharField(default='1qrZGQ', max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='attendance_id',
            field=models.CharField(default='FX1cAA', max_length=10),
        ),
    ]