from backdoor.models import Url

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
