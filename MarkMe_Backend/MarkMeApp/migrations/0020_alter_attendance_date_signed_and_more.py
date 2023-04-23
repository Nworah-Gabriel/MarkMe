# Generated by Django 4.1.8 on 2023-04-23 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarkMeApp', '0019_alter_attendance_date_signed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date_signed',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 23, 12, 46, 38, 474948)),
        ),
        migrations.AlterField(
            model_name='courses',
            name='academic_session',
            field=models.CharField(default=datetime.datetime(2023, 4, 23, 12, 46, 38, 473948), max_length=20),
        ),
        migrations.AlterField(
            model_name='courses',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 23, 12, 46, 38, 473948)),
        ),
        migrations.AlterField(
            model_name='institutions',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 23, 12, 46, 38, 474948)),
        ),
        migrations.AlterField(
            model_name='instructors',
            name='attendance_id',
            field=models.CharField(default='y2T5LQ', max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='attendance_id',
            field=models.CharField(default='-RfDpA', max_length=50),
        ),
    ]