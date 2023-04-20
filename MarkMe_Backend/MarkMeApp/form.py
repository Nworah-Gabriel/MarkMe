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
    institutions = forms.CharField(max_length=500)
    password = forms.CharField(max_length=50)


class StudentsForm(forms.Form):
    """
    A form class created for the students
    """

    username = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    institutions = forms.CharField(max_length=200)
    password = forms.CharField(max_length=50)


class GuardiansForm(forms.Form):
    """
    A form class created for the guardians
    """

    username = forms.CharField(max_length=200)
    email_address = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)


class CoursesForm(forms.Form):
    """
    A form class created for storing registering courses
    """

    name = forms.CharField(max_length=200)
    course_code = forms.CharField(max_length=20)


class InstitutionsForm(forms.Form):
    """
    A form class created for registering institutions
    """

    name = forms.CharField(max_length=500)
    Type = forms.CharField(max_length=100)

class loginForm(forms.Form):
    """
    A form class created for logging in users
    """

    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30)