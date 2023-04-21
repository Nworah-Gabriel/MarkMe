from django.contrib import admin
from django.urls import path
from .views import dashboard, attendance, StudentSignUp, InstructorSignUp, GuardianSignUp, loginView, logoutView, createInstitution

urlpatterns = [
    path('dashboard', dashboard.as_view(), name="dashboard"),
    path('attendance', attendance),
    path('StudentSignUp', StudentSignUp),
    path('InstructorSignUp', InstructorSignUp),
    path('GuardianSignUp', GuardianSignUp),
    path('login', loginView.as_view(), name="login"),
    path('logout', logoutView.as_view(), name="logout"),
    path('createInstitution', createInstitution),
]