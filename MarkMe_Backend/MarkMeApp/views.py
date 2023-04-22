from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from .form import loginForm, AttendanceForm, GuardiansForm, StudentsForm, InstructorsForm, InstitutionsForm, CoursesForm
from django.contrib.auth import login, logout
from django.views import View
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Guardians, Instructors, Students, Institutions, Courses, Attendance 
from uuid import uuid4
# Create your views here.

# def dashboard(request):
#     return render(request, "index.html")


def attendance(request):
    user = request.user
    attendance_list = ""
    
    try:
        get_user = Instructors.objects.get(unique_id=user.unique_id)
        attendance_list = get_user.attendance.all()
    except (Instructors.DoesNotExist, AttributeError):
        try:
            get_user = Students.objects.get(password=user.password)
            attendance_list = get_user.attendance.all()
        except Students.DoesNotExist:
            return render(request, "dashboard.html")
    return render(request, "attendance.html", {"attendances":attendance_list})

def createInstitution(request):
    form = InstitutionsForm(request.POST)

    # try:
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('dashboard')
    # except:
        # error = "Invalid form or Institution already exist"
        # return render(request, "InstitutionReg.html", {"user":form, "error":error})
    return render(request, "InstitutionReg.html", {"user":form})

#--USER SIGNUP AND LOGIN VIEWS ARE CREATED BELOW--#
def StudentSignUp(request):
    """
    A functional based view for student signup form
    """

    form = StudentsForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data["name"]
            institution = form.cleaned_data["institution"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]

            try:
                institute = Institutions.objects.get(name=institution)

                student = Students(
                    name=name,
                    username=username,
                    email=email,
                    institutions = institute,
                )
                student.set_password(password)
                student.save()
                return HttpResponseRedirect('login')
            
            except Institutions.DoesNotExist:
                error = "Institution does not exist"
                return render(request, 'login.html', {'user':form, 'error':error})
            
         
    return render(request, "StudentSignUp.html", {'user':form})


def InstructorSignUp(request):
    """
    A functional based view for instructor signup form
    """
    form = InstructorsForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data["name"]
            institution = form.cleaned_data["institution"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]

            try:
                institute = Institutions.objects.get(name=institution)

                instructor = Instructors(
                    name=name,
                    username=username,
                    email=email,
                    institutions = institute,
                )
                instructor.set_password(password)
                instructor.save()
                return HttpResponseRedirect('login')
            
            except Institutions.DoesNotExist:
                error = "Institution does not exist"
                return render(request, 'login.html', {'login':form, 'error':error})
            
         
    return render(request, "InstructorSignUp.html", {"user":form})


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
                email=email,
                unique_id=uuid4()
            )

            guardian.set_password(password)
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
        course = CoursesForm(request.POST)
        registeredCourses = ""
        attendance = AttendanceForm(request.POST)
        
        if isinstance(user, AnonymousUser):
            return HttpResponse("You cannot access this view")
        else:
            try:
                value = Guardians.objects.get(username=user.username)
            except Guardians.DoesNotExist:
                try:
                    value = Instructors.objects.get(username=user.username)
                    registeredCourses = value.courses.all()

                except Instructors.DoesNotExist:
                    try:

                        value = Students.objects.get(username=user.username)
                        registeredCourses = value.courses.all()

                    except Students.DoesNotExist:
                        return HttpResponseRedirect('login')

                                        
        return render(
            request,
            "dashboard.html",
            {"user":user,
            "id":str(value.email),
            "registeredCourses": registeredCourses,
            "course": course,
            "attendance": attendance,
            "instructor": "True",
            },
        )


    def post(self, request, *args, **kwargs):
        """
        A method for post request
        """
        user = request.user
        course = CoursesForm(request.POST)
        registeredCourses = ""
        attendance = AttendanceForm(request.POST)
        
        if request.method == 'POST':
            if attendance.is_valid():
                name = attendance.cleaned_data['course_title']
                academic_session = attendance.cleaned_data['academic_session']
                ID = attendance.cleaned_data['ID']

                try:
                    course_name = Courses.objects.get(name=name, academic_session=academic_session)
                    new_attendance = Attendance(
                        course=course_name,
                        academic_session=academic_session,
                    )
                    new_attendance.save()

                    student = Students.objects.get(attendance_id=ID)
                    student.attendance.add(new_attendance.id)
                    print(name, academic_session)
                
                except:
                    pass

        if request.method == 'POST':
            if course.is_valid():
                name = course.cleaned_data['name']
                acc = course.cleaned_data['academic_session']

                data = Courses(name=name, academic_session=acc)
                data.save()

                course_add = Instructors.objects.get(username=user.username)
                course_add.courses.add(data.id)
                course_add.save()


        try:
            value = Instructors.objects.get(username=user.username)
            registeredCourses = value.courses.all()
        
            return render(
            request,
            "dashboard.html",
            {"user":user,
            "id":str(value.email),
            "course": course,
            "attendance": attendance,
            "registeredCourses": registeredCourses,
            # "instructor": "True",
            },
        )

        except Instructors.DoesNotExist:
            pass
    
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