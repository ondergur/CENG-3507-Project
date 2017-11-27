from django.shortcuts import render


def index(request):
    context = {"asd": "asd"}
    return render(request, 'app_lecturer/index.html', context)
