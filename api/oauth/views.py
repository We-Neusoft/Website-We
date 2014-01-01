from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from api.oauth.models import RedirectionUri
from api.oauth.forms import AuthorizeForm

def authorize(request):
    if 'username' not in request.POST or 'password' not in request.POST:
        try:
            response_type = request.REQUEST['response_type']
            client_id = request.REQUEST['client_id']
        except KeyError:
            return HttpResponse('Invalid_request')

        try:
            client = User.objects.get(username=client_id)
            client.groups.get(name='oauth')
        except (User.DoesNotExist, Group.DoesNotExist):
            return HttpResponse('Invalid client id.')

        redirect_uri = request.REQUEST.get('redirect_uri', '')
        try:
            RedirectionUri.objects.filter(client=client).get(uri=redirect_uri)
        except RedirectionUri.DoesNotExist:
            return HttpResponse('Mismatching redirection URI.')

        scope = request.REQUEST.get('scope', '')
        state = request.REQUEST.get('state', '')

        request.session.set_expiry(0)
        request.session['client_id'] = client_id
        request.session['redirect_uri'] = redirect_uri
        request.session['scope'] = scope
        request.session['state'] = state

        return render_to_response('api/oauth/authorize.html', csrf(request))
    else:
        client_id = request.session['client_id']
        redirect_uri = request.session['redirect_uri']
        scope = request.session['scope']
        state = request.session['state']

        form = AuthorizeForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            if authenticate(email=username, password=password):
                code = '123'
                uri = redirect_uri + '?code=' + code
                if state:
                    uri += '&state=' + state

                return HttpResponseRedirect(uri)

        return HttpResponse('Failure')
