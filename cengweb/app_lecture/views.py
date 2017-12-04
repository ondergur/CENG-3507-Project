from django.shortcuts import render
from .models import Lecture


def homepage(request):
    context = {"asd": "asd"}
    return render(request, 'homepage.html', context)


def classone(request):
    lectures = Lecture.objects.filter(year='1')
    context = {"lectures": lectures}
    return render(request, 'classone.html', context)
