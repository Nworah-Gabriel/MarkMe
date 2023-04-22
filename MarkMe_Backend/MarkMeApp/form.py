"""
A module that handles forms
"""
from django import forms
from django.forms import ModelForm
from .models import Institutions, Courses, Attendance


class InstructorsForm(forms.Form):
    """
    A form class created for the instructors
    """

    name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=100)
    institution = forms.CharField(max_length=500)
    password = forms.CharField(max_length=50)


class StudentsForm(forms.Form):
    """
    A form class created for the students
    """
    name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=100)
    institution = forms.CharField(max_length=200)
    password = forms.CharField(max_length=50)


class GuardiansForm(forms.Form):
    """
    A form class created for the guardians
    """

    username = forms.CharField(max_length=200)
    email_address = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)


class CoursesForm(ModelForm):
    """
    A form class created for storing registering courses
    """

    
    class Meta:
        model = Courses
        fields = ["name", "academic_session"]


class InstitutionsForm(ModelForm):
    """
    A model form class created for registering institutions
    """
    class Meta:
        model = Institutions
        fields = ["name", "Type"]


class AttendanceForm(forms.Form):
    """
    A model form class created for registering institutions
    """
    
    
    course_title = forms.CharField(max_length=50)
    academic_session = forms.CharField(max_length=20)
    ID = forms.CharField(max_length=20)


class loginForm(forms.Form):
    """
    A form class created for logging in users
    """

    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30)