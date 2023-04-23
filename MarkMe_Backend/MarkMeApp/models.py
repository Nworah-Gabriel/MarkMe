from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid
from secrets import token_urlsafe

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
    attendance_id = models.CharField(max_length=10, default=token_urlsafe(4))

   
class Students(User):
    """
    A model class created for the students
    """


    name = models.CharField(max_length=200)
    courses = models.ManyToManyField(to="Courses")
    unique_id = models.UUIDField(default=uuid.uuid4)
    institutions = models.ForeignKey(to="Institutions", on_delete=models.DO_NOTHING)
    attendance = models.ManyToManyField(to="Attendance")
    attendance_id = models.CharField(max_length=50, default=token_urlsafe(4))


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
    course_id = models.CharField(max_length=50 ,default=token_urlsafe(8))
    academic_session = models.CharField(max_length=4)


    def __str__(self):
        """
        A string representation of the created object
        """

        return self.name


class Institutions(models.Model):
    """
    A model class created for storing institution records in the database
    """

    choice = (
        ("Primary", "Primary"),
        ("Secondary", "Secondary"),
        ("Tetiary", "Tetiary")
    )

    name = models.CharField(max_length=500, unique=True)
    unique_id = models.UUIDField(default=uuid.uuid4)
    date_created = models.DateTimeField(default=datetime.now())
    Type = models.CharField(max_length=100, choices=choice)


    def __str__(self):
        """
        A string representation of the created object
        """

        return self.name


class Attendance(models.Model):
    """
    A model class for storing attendance record for each student
    """

    course = models.ForeignKey(to="Courses", on_delete=models.CASCADE)
    date_signed = models.DateTimeField(default=datetime.now())
    unique_id = models.UUIDField(default=uuid.uuid4)
    academic_session = models.CharField(max_length=20)


    def __str__(self):
        """
        A string representation of the created object
        """

        return self.course.name