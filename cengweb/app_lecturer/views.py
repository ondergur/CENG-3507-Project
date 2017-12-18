from django.shortcuts import render
from .models import Lecturer


def index(request):
    lecturers = Lecturer.objects.filter(bolum='Bilgisayar Mühendisliği')
    context = {"lecturers": lecturers}
    return render(request, 'lecturer/index.html', context)

