from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse

from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

CLIENT_ID = settings.OPEN_CLIENT_ID
CLIENT_SECRET = settings.OPEN_CLIENT_SECRET
OPEN_AUTHORIZE_URL = settings.OPEN_SERVER_AUTHORIZE
OPEN_TOKEN_URL = settings.OPEN_SERVER_TOKEN
OPEN_GET_USER_INFO_URL = settings.OPEN_SERVER_USER_GET_INFO
OPEN_GET_USER_EMAIL_URL = settings.OPEN_SERVER_USER_GET_EMAIL

def login(request, redirect_uri, scope):
    cloud = OAuth2Session(CLIENT_ID, redirect_uri=redirect_uri, state=request.GET.get('state', None), scope=scope)

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

def get_user_email(request):
    cloud = OAuth2Session(CLIENT_ID, token=request.session['oauth_token'])

    result = cloud.get(OPEN_GET_USER_EMAIL_URL).text
    if result.lower() == 'none':
        return None
    else:
        return result
