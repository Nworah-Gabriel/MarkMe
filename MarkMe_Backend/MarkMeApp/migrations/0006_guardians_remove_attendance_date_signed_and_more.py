# Generated by Django 4.1.6 on 2023-04-18 02:13

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('MarkMeApp', '0005_remove_students_attendance_remove_students_courses_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guardians',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('unique_id', models.UUIDField(default=uuid.uuid4)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='date_signed',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='institutions',
            name='date_created',
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=200)),
                ('unique_id', models.UUIDField(default=uuid.uuid4)),
                ('attendance', models.ManyToManyField(to='MarkMeApp.attendance')),
                ('courses', models.ManyToManyField(to='MarkMeApp.courses')),
                ('institutions', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MarkMeApp.institutions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Instructors',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=200)),
                ('unique_id', models.UUIDField(default=uuid.uuid4)),
                ('attendance', models.ManyToManyField(to='MarkMeApp.attendance')),
                ('courses', models.ManyToManyField(to='MarkMeApp.courses')),
                ('institutions', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='MarkMeApp.institutions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]