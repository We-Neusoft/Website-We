from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

import datetime

from api.oauth.models import AuthorizationCode, Client, RedirectionUri
from api.oauth.forms import AuthenticationForm, InitializationForm

def authorize(request):
    form = AuthenticationForm(request.POST)

    if not form.is_valid():
        form, client = verify_client(request.REQUEST)
        if issubclass(form.__class__, HttpResponse):
             return form

        scope = form.cleaned_data['scope']
        state = form.cleaned_data['state']

        request.session.set_expiry(0)
        request.session.update(form.cleaned_data)

        return render_to_response('api/oauth/authorize.html', csrf(request))
    else:
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        form, client = verify_client(request.REQUEST)
        if issubclass(form.__class__, HttpResponse):
             return form

        response_type = form.cleaned_data['response_type']
        client_id = form.cleaned_data['client_id']
        redirect_uri = request.session['redirect_uri']
        scope = request.session['scope']
        state = request.session['state']

        user = authenticate(email=username, password=password)
        if user:
            code = AuthorizationCode(client=client, user=user, redirect_uri=redirect_uri, expire_time=datetime.datetime.now() + datetime.timedelta(minutes=10))
            code.save()

            return callback_client(redirect_uri + '?code=' + code.code.encode(), state)

        return HttpResponse('Failure')

def token(request):
    if not 'REMOTE_USER' in request.META:
        #response = HttpResponse('401 Unauthorized', status=401)
        response = HttpResponse(request.META.items(), status=401)
        response['WWW-Authenticate'] = 'Basic realm="Please provide your client_id and client_secret."'
        return response

def verify_client(form):
    form = InitializationForm(form)
    if not form.is_valid():
        return HttpResponse('Invalid_request'), None

    state = form.cleaned_data['state']

    client_id = form.cleaned_data['client_id']
    try:
        client = Client.objects.get(client_id=client_id)
    except (Client.DoesNotExist):
        return HttpResponse('Invalid client id.'), None

    redirect_uri = form.cleaned_data['redirect_uri']
    try:
        RedirectionUri.objects.filter(client=client).get(redirect_uri=redirect_uri)
    except RedirectionUri.DoesNotExist:
        return HttpResponse('Mismatching redirection URI.'), client

    response_type = form.cleaned_data['response_type']
    if not response_type in ['code']:
        return callback_client(redirect_uri + '?error=unsupported_response_type', state), None

    return form, client

def callback_client(uri, state):
    if state:
        uri += '&state=' + state

    return HttpResponseRedirect(uri)
