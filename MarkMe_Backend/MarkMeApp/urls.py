from django.contrib import admin
from django.urls import path
from .views import dashboard, attendance

urlpatterns = [
    path('dashboard', dashboard),
    path('attendance', attendance)
]