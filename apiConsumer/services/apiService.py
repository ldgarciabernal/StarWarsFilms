import requests
from django.conf import settings

def get_all(prefix):
    response = requests.get("{0}/{1}/".format(
        settings.BASE_API_URL, prefix))
    if response.status_code != 200:
        return None
    return response

def get(prefix, param):
    response = requests.get("{0}/{1}/{2}/".format(
        settings.BASE_API_URL, prefix, param))
    if response.status_code != 200:
        return None
    return response

def get_by_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response