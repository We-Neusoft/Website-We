from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse

from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

CLIENT_ID = getattr(settings, 'OPEN_CLIENT_ID')
CLIENT_SECRET = getattr(settings, 'OPEN_CLIENT_SECRET')
OPEN_AUTHORIZE_URL = getattr(settings, 'OPEN_SERVER_AUTHORIZE')
OPEN_TOKEN_URL = getattr(settings, 'OPEN_SERVER_TOKEN')
OPEN_GET_USER_INFO_URL = getattr(settings, 'OPEN_SERVER_USER_GET_INFO')
OPEN_GET_USER_PRIVACY_URL = getattr(settings, 'OPEN_SERVER_USER_GET_PRIVACY')

def login(request, redirect_uri):
    cloud = OAuth2Session(CLIENT_ID, redirect_uri=redirect_uri, state=request.GET.get('state', None))

    authorization_url, state = cloud.authorization_url(OPEN_AUTHORIZE_URL)
    request.session['oauth_state'] = state

    return HttpResponseRedirect(authorization_url)

def get_token(request, redirect_uri, code):
    cloud = OAuth2Session(CLIENT_ID, redirect_uri=redirect_uri, state=request.session['oauth_state'])

    token = cloud.fetch_token(OPEN_TOKEN_URL, code=code, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET))
    request.session['oauth_token'] = token

    return True

def logout(request):
    del request.session['oauth_state']
    del request.session['oauth_token']

def get_user_info(request):
    cloud = OAuth2Session(CLIENT_ID, token=request.session['oauth_token'])

    result = cloud.get(OPEN_GET_USER_INFO_URL).text
    if result.lower() == 'none':
        return None
    else:
        return result

def get_user_privacy(request):
    cloud = OAuth2Session(CLIENT_ID, token=request.session['oauth_token'])

    result = cloud.get(OPEN_GET_USER_PRIVACY_URL).text
    if result.lower() == 'none':
        return None
    else:
        return result
