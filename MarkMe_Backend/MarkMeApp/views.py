from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from .form import loginForm, GuardiansForm, StudentsForm, InstructorsForm, InstitutionsForm, CoursesForm
from django.contrib.auth import login, logout
from django.views import View
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Guardians, Instructors, Students, Institutions, Courses, Attendance 
# Create your views here.

# def dashboard(request):
#     return render(request, "index.html")


def attendance(request):
    return render(request, "attendance.html")



#--USER SIGNUP AND LOGIN VIEWS ARE CREATED BELOW--#
def StudentSignUp(request):
    """
    A functional based view for student signup form
    """

    return render(request, "StudentSignUp.html")


def InstructorSignUp(request):
    """
    A functional based view for instructor signup form
    """

    return render(request, "InstructorSignUp.html")


def GuardianSignUp(request):
    """
    A functional based view for guardian signup form
    """
    form = GuardiansForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email_address"]

            guardian = Guardians(
                username=username,
                password=password,
                email=email,
            )
            guardian.save()
            return HttpResponseRedirect('login')
    return render(request, "GuardiansSignUp.html", {"user": form})

class loginView(View):
    """A class that handles the login view"""
    form_class = loginForm

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def get(self, request, *args, **kwargs):
        """A function for logging in"""
        form = self.form_class()
        return render(request, 'login.html', {'login':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("dashboard")
            else:
                return render(request, 'login.html', {'login':form, 'error':'Invalid details'})
        else:
            return HttpResponse('The form is not valid')


class dashboard(LoginRequiredMixin, View):
    """A class that handles the protected view"""

    login_url = "login"
    redirect_field_name = "redirected"
    permission_denied_message = "You're not an authenticated user"

    def get(self, request, *args, **kwargs):
        """A function for getting protected information"""
        
        user = request.user

        if isinstance(user, AnonymousUser):
            return HttpResponse("You cannot access this view")
        else:
            return render(request, "dashboard.html", {"user":user})


class logoutView(View):
    """A class that handles the logout view"""

    def get(self, request, *args, **kwargs):
        """A function for logging out"""
        user = request.user
        if isinstance(user, AnonymousUser):
            return HttpResponse('You\'re not logged in!!!')
        else:
            logout(request)
            return HttpResponseRedirect("login")