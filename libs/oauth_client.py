from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

import urllib2
from urllib import urlencode
from json import loads

from oauth_forms import TokenForm

CLIENT_ID = getattr(settings, 'OPEN_CLIENT_ID')
CLIENT_SECRET = getattr(settings, 'OPEN_CLIENT_SECRET')
OPEN_AUTHORIZE_URL = getattr(settings, 'OPEN_SERVER_AUTHORIZE')
OPEN_TOKEN_URL = getattr(settings, 'OPEN_SERVER_TOKEN')

def login(request, redirect_uri):
    form = TokenForm(request.session)
    if not form.is_valid():
        request.session.clear()
        request.session.set_expiry(0)

        params = {
            'response_type': 'code',
            'client_id': CLIENT_ID,
            'redirect_uri': redirect_uri,
            'state': 'wecloud',
        }

        return HttpResponseRedirect(OPEN_AUTHORIZE_URL + '?%s' % urlencode(params))

def get_token(request, redirect_uri, code):
    params = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
    }
    url = OPEN_TOKEN_URL

    basic_auth = urllib2.HTTPBasicAuthHandler()
    basic_auth.add_password(realm='Please provide your client_id and client_secret.', uri=url, user=CLIENT_ID, passwd=CLIENT_SECRET)
    urllib2.install_opener(urllib2.build_opener(basic_auth))

    auth_request = urllib2.Request(url)
    auth_request.add_data(urlencode(params))

    try:
        token = loads(urllib2.urlopen(auth_request).read())
        request.session.clear()
        request.session.set_expiry(None)
        request.session.update({'type': token['token_type'], 'token': token['access_token']})

        return True
    except urllib2.HTTPError:
        return False
