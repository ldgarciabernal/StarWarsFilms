import requests
import json
from django.conf import settings
from apiConsumer.services import apiService

def get_film_by_title(prefix, title):
    response = apiService.get_all(prefix)
    if response == None:
        return []
    
    film = list(filter(lambda x : x["title"] == title, response.json()["results"]))
    if film != []:
        return film[0]

    return film


def get_films_title(prefix):
    response = apiService.get_all(prefix)
    if response == None:
        return []
    
    films_title = list(map(lambda x : x["title"], response.json()["results"]))
    return films_title