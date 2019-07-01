from django.shortcuts import render

# Create your views here.

def seacrh_film(request):
    return render(request, 'searchFilm.html')