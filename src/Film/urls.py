from django.contrib import admin
from django.urls import path, include
from film import views

urlpatterns = [
    path('', views.seacrh_film, name='searchFilms')
]
