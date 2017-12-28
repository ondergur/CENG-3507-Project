from django.shortcuts import render
from .models import Lecture
from .forms import QuestionForm


def homepage(request):
    context = {"asd": "asd"}
    return render(request, 'homepage.html', context)


def report(request):
    context = {"asd": "asd"}
    return render(request, 'report.html', context)


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
    code = str.replace(code, "-", " ").upper()
    lecture = Lecture.objects.filter(pk=code)
    print(type(lecture))
    hoca = ""
    for i in lecture:
        hoca = i.lecturer

    all_lectures = Lecture.objects.filter(lecturer=hoca)
    context = {"lecture": lecture, "dersler": all_lectures}
    return render(request, 'lecture/detail.html', context)


def candidate(request):
    if request.POST:
        form = QuestionForm(request.POST)
        form.save()
    else:
        form = QuestionForm()
    return render(request, 'candidate.html',
                  {'form': form, }
                  )


