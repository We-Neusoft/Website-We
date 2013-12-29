from django.http import HttpResponse, HttpResponseRedirect

def authorize(request):
    try:
        response_type = request.REQUEST['response_type']
        client_id = request.REQUEST['client_id']
    except KeyError:
        return HttpResponse('invalid_request')

    redirect_uri = request.REQUEST.get('redirect_uri', '')
    scope = request.REQUEST.get('scope', '')
    state = request.REQUEST.get('state', '')

    request.session['client_id'] = client_id
    request.session.set_expiry(0)
    return HttpResponse(request.session.items())
