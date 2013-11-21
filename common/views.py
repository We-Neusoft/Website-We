from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

import json

from we.utils.navbar import get_username

def get_user(request):
    return HttpResponse(json.dumps(get_username(request)), 'application/json');
