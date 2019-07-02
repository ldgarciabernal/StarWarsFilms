from django.shortcuts import render
from apiConsumer.services import filmService

# Create your views here.

def detail_film(request):
    request_response = request.POST.get('film_name')

    film = filmService.get_film_by_title('films', request_response)
    context = {}
    context['film'] = film
    
    return render(request, 'detail.html', context=context)