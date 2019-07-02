import requests
import json
from django.conf import settings
from apiConsumer.services import apiService


def get_people(prefix):
    response = apiService.get_all(prefix)
    if response == None:
        return []
    
    people = list(response.json()["results"])
    return people

def get_person(url):
    response = apiService.get_by_url(url)
    if response == None:
        return []

    person = response.json()
    return person