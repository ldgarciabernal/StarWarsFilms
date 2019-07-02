from django.shortcuts import render
from apiConsumer.services import personService, filmService
from film.forms.filmform import FilmForm

# Create your views here.

def seacrh_film(request):
    context = {}
    context['people'] = personService.get_people('people')
    context['films_name'] = filmService.get_films_title('films')

    form = FilmForm()
    context['form'] = form

    return render(request, 'searchFilm.html', context=context)