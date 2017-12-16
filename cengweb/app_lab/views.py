from django.shortcuts import render
from .models import Lab


def index(request):
    labs = Lab.objects.all()
    context = {"labs": labs}
    return render(request, 'lab/index.html', context)
