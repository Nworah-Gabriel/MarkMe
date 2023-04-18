from django.contrib import admin
from .models import Instructors, Students, Guardians, Courses, Institutions, Attendance

# Register your models here.
admin.site.register(Instructors)
admin.site.register(Institutions)
admin.site.register(Students)
admin.site.register(Guardians)
admin.site.register(Courses)
admin.site.register(Attendance)