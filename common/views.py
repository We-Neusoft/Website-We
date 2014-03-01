from django.http import HttpResponse

import json

from navigation import get_username

def get_user(request):
    return HttpResponse(json.dumps(get_username(request)), 'application/json');
