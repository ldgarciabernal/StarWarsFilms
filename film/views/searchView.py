from django.shortcuts import render
from apiConsumer.services import personService, filmService

# Create your views here.

def seacrh_film(request):
    context = {}
    context['people'] = personService.get_people('people')
    context['films_name'] = filmService.get_films_title('films')

    return render(request, 'searchFilm.html', context=context)