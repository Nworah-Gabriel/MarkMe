"""
A module that handles forms
"""
from django import forms

class InstructorsForm(forms.Form):
    """
    A form class created for the instructors
    """

    username = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    institutions = models.CharField(max_length=500)
    password = models.CharField(max_length=50)


class StudentsForm(forms.Form):
    """
    A form class created for the students
    """

    username = models.CharField(max_length=200)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    institutions = forms.CharField(max_length=200)
    password = forms.CharField(max_length=50)


class Guardians(forms.Form):
    """
    A form class created for the guardians
    """

    username = models.CharField(max_length=200)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)


class Courses(forms.Form):
    """
    A form class created for storing registering courses
    """

    name = models.CharField(max_length=200)
    course_code = models.CharField(null=True, blank=True, max_length=20)


class Institutions(forms.Form):
    """
    A form class created for registering institutions
    """

    name = models.CharField(max_length=500)
    Type = models.CharField(max_length=100, choices=choice)