import requests
import json
from django.conf import settings
from apiService import get_all

def get_films_title(prefix):
    response = get_all(prefix)
    films = json.loads(response)
    if films == None:
        return []
    
    films_title = map(lambda x : x["title"], films.json()["results"])
    return list(films_title)
    