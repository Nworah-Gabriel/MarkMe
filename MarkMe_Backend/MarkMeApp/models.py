from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid


# Create your models here.

class Instructors(User):
    """
    A model class created for the instructors
    """


    name = models.CharField(max_length=200)
    courses = models.ManyToManyField(to="Courses")
    unique_id = models.UUIDField(default=uuid.uuid4)
    institutions = models.ForeignKey(to="Institutions", on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(to="Attendance")


class Students(User):
    """
    A model class created for the students
    """


    name = models.CharField(max_length=200)
    courses = models.ManyToManyField(to="Courses")
    unique_id = models.UUIDField(default=uuid.uuid4)
    institutions = models.ForeignKey(to="Institutions", on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(to="Attendance")


class Guardians(User):
    """
    A model class created for the guardians
    """


    unique_id = models.UUIDField(default=uuid.uuid4)


class Courses(models.Model):
    """
    A model class created for storing course record in the database
    """


    name = models.CharField(max_length=200)
    course_code = models.CharField(null=True, blank=True, max_length=20)
    date_created = models.DateTimeField(default=datetime.now())
    unique_id = models.UUIDField(default=uuid.uuid4)


class Institutions(models.Model):
    """
    A model class created for storing institution records in the database
    """

    choice = (
        ("Primary", "primary"),
        ("Secondary", "secondary"),
        ("Tetiary", "tetiary")
    )

    name = models.CharField(max_length=500)
    unique_id = models.UUIDField(default=uuid.uuid4)
    date_created = models.DateTimeField(default=datetime.now())
    Type = models.CharField(max_length=100, choices=choice)


class Attendance(models.Model):
    """
    A model class for storing attendance record for each student
    """

    course = models.ForeignKey(to="Courses", on_delete=models.CASCADE)
    date_signed = models.DateTimeField(default=datetime.now())
    unique_id = models.UUIDField(default=uuid.uuid4)