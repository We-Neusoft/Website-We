from django.core.cache import cache
from django.http import HttpResponse
from django.views import generic

import json
from markdown import markdown

from ip import get_geo
from navigation import get_navbar, get_username

from .models import NavbarItem, NavbarMore

def get_user(request):
    return HttpResponse(json.dumps(get_username(request)), 'application/json');
