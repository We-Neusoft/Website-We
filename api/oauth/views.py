from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from api.oauth.models import RedirectionUri
from api.oauth.forms import AuthenticationForm, InitializationForm

def authorize(request):
    form = AuthenticationForm(request.POST)

    if not form.is_valid():
        form = verify_client(request.REQUEST)
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

        form = verify_client(request.REQUEST)
        if issubclass(form.__class__, HttpResponse):
             return form

        response_type = form.cleaned_data['response_type']
        client_id = form.cleaned_data['client_id']
        redirect_uri = request.session['redirect_uri']
        scope = request.session['scope']
        state = request.session['state']

        user = authenticate(email=username, password=password)

        if user:
            code = '123'

            return callback_client(redirect_uri + '?code=' + code, state)

        return HttpResponse('Failure')

def verify_client(form):
    form = InitializationForm(form)
    if not form.is_valid():
        return HttpResponse('Invalid_request')

    state = form.cleaned_data['state']

    client_id = form.cleaned_data['client_id']
    try:
        client = User.objects.get(username=client_id)
        client.groups.get(name='oauth')
    except (User.DoesNotExist, Group.DoesNotExist):
        return HttpResponse('Invalid client id.')

    redirect_uri = form.cleaned_data['redirect_uri']
    try:
        RedirectionUri.objects.filter(client=client).get(uri=redirect_uri)
    except RedirectionUri.DoesNotExist:
        return HttpResponse('Mismatching redirection URI.')

    response_type = form.cleaned_data['response_type']
    if not response_type in ['code']:
        return callback_client(redirect_uri + '?error=unsupported_response_type', state)

    return form

def callback_client(uri, state):
    if state:
        uri += '&state=' + state

    return HttpResponseRedirect(uri)
