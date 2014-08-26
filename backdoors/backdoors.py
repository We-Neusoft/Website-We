from referer.models import Url

from ip import get_geo
from urlparse import urlparse

def validate_referer(request):
    referer = request.META.get('HTTP_REFERER')

    if not referer:
        return False
    url = urlparse(referer)

    try:
        Url.objects.filter(enable=True).get(url=(url.scheme + '://' + url.netloc + url.path))
        return True
    except Url.DoesNotExist:
        return False

def validate_ip(request):
    return get_geo(request)[:6] == 'server'
