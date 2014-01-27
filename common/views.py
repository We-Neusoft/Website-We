from django.http import HttpResponse

import json

from libs.navigation import get_username

def get_user(request):
    return HttpResponse(json.dumps(get_username(request)), 'application/json');
