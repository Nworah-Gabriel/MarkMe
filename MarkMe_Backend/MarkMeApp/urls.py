from django.contrib import admin
from django.urls import path
from .views import dashboard, home, delete, attendance, StudentSignUp, InstructorSignUp, GuardianSignUp, loginView, logoutView, createInstitution

urlpatterns = [
    path('dashboard', dashboard.as_view(), name="dashboard"),
    path('attendance', attendance),
    path('StudentSignUp', StudentSignUp),
    path('InstructorSignUp', InstructorSignUp),
    path('GuardianSignUp', GuardianSignUp),
    path('login', loginView.as_view(), name="login"),
    path('logout', logoutView.as_view(), name="logout"),
    path('createInstitution', createInstitution),
    path('delete/<str:course_id>/<str:academic_session>', delete),
    path("", home)
    
]