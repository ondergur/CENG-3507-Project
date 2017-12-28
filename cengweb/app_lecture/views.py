from django.shortcuts import render
from .models import Lecture


def homepage(request):
    context = {"asd": "asd"}
    return render(request, 'homepage.html', context)


def candidate(request):
    context = {"asd": "asd"}
    return render(request, 'candidate.html', context)


def classone(request):
    lectures = Lecture.objects.filter(year='1')
    context = {"lectures": lectures}
    return render(request, 'lecture/classes.html', context)


def classtwo(request):
    lectures = Lecture.objects.filter(year='2')
    context = {"lectures": lectures}
    return render(request, 'lecture/classes.html', context)


def classthree(request):
    lectures = Lecture.objects.filter(year='3')
    context = {"lectures": lectures}
    return render(request, 'lecture/classes.html', context)


def classfour(request):
    lectures = Lecture.objects.filter(year='4')
    context = {"lectures": lectures}
    return render(request, 'lecture/classes.html', context)


def details(request, code):
    print(code)
    code = str.replace(code, "-", " ").upper()
    print(code)
    lecture = Lecture.objects.filter(pk=code)
    context = {"lecture": lecture}
    print(lecture)
    return render(request, 'lecture/detail.html', context)

