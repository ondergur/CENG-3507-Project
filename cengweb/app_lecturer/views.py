from django.shortcuts import render
from .models import Lecturer


def index(request):
    context = {"asd": "asd"}
    return render(request, 'lecturer/index.html', context)


def lecturers(request):
    lecturer = Lecturer.objects.all()
    context = {"lecturer": lecturer}
    return render(request, 'index.html', context)
