from django.shortcuts import render
from .models import Student

def list_students(request):
    students = Student.objects.all()
    return render(request, 'main/home.html', {'students': students})