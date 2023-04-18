from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, "index.html")


def attendance(request):
    return render(request, "attendance.html")