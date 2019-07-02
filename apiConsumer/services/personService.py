import requests
import json
from django.conf import settings
from apiService import get_all, get_by_url


def get_people(prefix):
    response = get_all(prefix)
    if response == None:
        return []
    
    people = list(response.json()["results"])
    return people

def get_person(url):
    response = get_by_url(url)
    if response == None:
        return []

    person = response.json()
    return person