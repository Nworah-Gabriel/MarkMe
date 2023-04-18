# Generated by Django 4.1.7 on 2023-04-18 02:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarkMeApp', '0006_guardians_remove_attendance_date_signed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='date_signed',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 3, 18, 43, 416415)),
        ),
        migrations.AddField(
            model_name='courses',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 3, 18, 43, 410254)),
        ),
        migrations.AddField(
            model_name='institutions',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 18, 3, 18, 43, 413290)),
        ),
    ]