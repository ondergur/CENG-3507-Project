from django.shortcuts import render
from .models import Lecture


def homepage(request):
    context = {"asd": "asd"}
    return render(request, 'homepage.html', context)


def classone(request):
    lectures = Lecture.objects.filter(year='1')
    context = {"lectures": lectures}
    return render(request, 'lecture/classone.html', context)


def classtwo(request):
    lectures = Lecture.objects.filter(year='2')
    context = {"lectures": lectures}
    return render(request, 'lecture/classtwo.html', context)


def classthree(request):
    lectures = Lecture.objects.filter(year='3')
    context = {"lectures": lectures}
    return render(request, 'lecture/classthree.html', context)


def classfour(request):
    lectures = Lecture.objects.filter(year='4')
    context = {"lectures": lectures}
    return render(request, 'lecture/classfour.html', context)

def developers(request):
    asd = ["Ahmet", "Ozan"]
    context = {"asd": asd}
    return render(request, 'developers.html', context)
