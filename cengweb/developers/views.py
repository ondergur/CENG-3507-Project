from django.shortcuts import render
from .forms import CommentForm


def developers(request):
    if request.POST:
        form = CommentForm(request.POST)
        form.save()
    else:
        form = CommentForm()
    return render(request, 'developers/developers.html',
                  {'form': form, }
                  )


