from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

import urllib, urllib2
from json import loads

from oauth_forms import TokenForm

CLIENT_ID = getattr(settings, 'OPEN_CLIENT_ID')
CLIENT_SECRET = getattr(settings, 'OPEN_CLIENT_SECRET')
OPEN_AUTHORIZE_URL = getattr(settings, 'OPEN_SERVER_AUTHORIZE')
OPEN_TOKEN_URL = getattr(settings, 'OPEN_SERVER_TOKEN')
OPEN_GET_USER_INFO_URL = getattr(settings, 'OPEN_SERVER_USER_GET_INFO')
OPEN_GET_USER_PRIVACY_URL = getattr(settings, 'OPEN_SERVER_USER_GET_PRIVACY')

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

        return HttpResponseRedirect(OPEN_AUTHORIZE_URL + '?%s' % urllib.urlencode(params))

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
    auth_request.add_data(urllib.urlencode(params))

    try:
        token = loads(urllib2.urlopen(auth_request).read())
        request.session.clear()
        request.session.set_expiry(None)
        request.session.update({'type': token['token_type'], 'token': token['access_token']})

        return True
    except urllib2.HTTPError:
        return False

def get_user_info(request, token):
    url = OPEN_GET_USER_INFO_URL

    request = urllib2.Request(url)
    request.add_header('Authorization', 'Bearer ' + token)

    result = urllib2.urlopen(request).read()
    if result.lower() == 'none':
        return None
    else:
        return result

def get_user_privacy(request, token):
    url = OPEN_GET_USER_PRIVACY_URL

    request = urllib2.Request(url)
    request.add_header('Authorization', 'Bearer ' + token)

    result = urllib2.urlopen(request).read()
    if result.lower() == 'none':
        return None
    else:
        return result
