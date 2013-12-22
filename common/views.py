from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

import json
import qrcode

from we.utils.navbar import get_username

def get_user(request):
    return HttpResponse(json.dumps(get_username(request)), 'application/json');

def qr(request):
    qr = qrcode.QRCode(box_size=2, border=0)
    qr.add_data(request.META.get('HTTP_REFERER'))
    qr_image = qr.make_image()
    response = HttpResponse(content_type='image/png')
    qr_image.save(response, 'PNG')
    return response
