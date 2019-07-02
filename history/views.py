from django.shortcuts import render
import datetime
from django.conf import settings

# Create your views here.


def set_cookie(response, key, value):
    response.set_cookie(key, value)


def get_current_history():
    return []