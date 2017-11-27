from django.shortcuts import render


def homepage(request):
    context = {"asd": "asd"}
    return render(request, 'base.html', context)


def index(request):
    context = {"asd": "asd"}
    return render(request, 'app_lecture/index.html', context)
