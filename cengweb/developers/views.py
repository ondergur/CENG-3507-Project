from django.shortcuts import render

def developers(request):
    asd = ["Ahmet", "Ozan"]
    context = {"asd": asd}
    return render(request, 'developers/developers.html', context)
