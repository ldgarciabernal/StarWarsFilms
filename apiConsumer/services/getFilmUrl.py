import requests
import json
from django.conf import settings
from apiService import get_all

def get_film_by_title(prefix, title):
    response = get_all(prefix)
    films = json.loads(response)
    if films == None:
        return []
    
    film = filter(lambda x : x["title"] == title, films.json()["results"])
    return list(film)
    
    