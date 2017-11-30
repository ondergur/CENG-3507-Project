from django.shortcuts import render
from .models import Lecture


def homepage(request):
    context = {"asd": "asd"}
    return render(request, 'base.html', context)


def classone(request):
    all_lectures = list(Lecture.objects.all())
    context = {"all_lectures": all_lectures}
    return render(request,
                  'classone.html',
                  context)
