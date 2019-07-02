from django.shortcuts import render

# Create your views here.

def detail_film(request):
    return render(request, 'detail.html')