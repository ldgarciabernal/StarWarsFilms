from django.contrib import admin
from django.urls import path, include
from film.views import searchView, detailView

urlpatterns = [
    path('', searchView.seacrh_film, name='searchFilms'),
    path('detail/', detailView.detail_film, name='detailFilm')
]
