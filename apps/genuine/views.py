#encoding=utf8
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render_to_response, redirect

import json
import requests

from libs import oauth_client
from navigation import get_navbar

DATA_ROOT = getattr(settings, 'DATA_ROOT', '/data/www/source')

DREAMSPARK_ACCOUNT = getattr(settings, 'DREAMSPARK_ACCOUNT')
DREAMSPARK_KEY = getattr(settings, 'DREAMSPARK_KEY')

OPEN_LOGIN_REDIRECT_URI = getattr(settings, 'DREAMSPARK_OPEN_REDIRECT_URI')

def index(request):
    result = get_navbar(request)

    return render_to_response('genuine/index.html', result)

def iuv(request):
    if 'action' in request.GET:
        action = request.GET['action']

        if request.GET['action'] == 'signin':
            return oauth_client.login(request, OPEN_LOGIN_REDIRECT_URI)

        elif request.GET['action'] == 'signout':
            return redirect('http://e5.onthehub.com/d.ashx?s=jlg1p270bi')

    if 'code' in request.GET:
        code = request.GET['code']

        if oauth_client.get_token(request, OPEN_LOGIN_REDIRECT_URI, code):
            email = json.loads(oauth_client.get_user_privacy(request))['email']
            oauth_client.logout(request)

            domain = email.split('@')[1]
            if domain.lower() == 'nou.com.cn':
                statuses = 'students'
            elif domain.lower() == 'neusoft.edu.cn':
                statuses = 'faculty,staff'

            payload = {
                'account': DREAMSPARK_ACCOUNT,
                'key': DREAMSPARK_KEY,
                'username': email,
                'academic_statuses': statuses,
                'email': email,
            }

            try:
                r = requests.get('https://e5.onthehub.com/WebStore/Security/AuthenticateUser.aspx', params=payload)

                if r.status_code == requests.codes.ok:
                    return redirect(r.text)
                else:
                    return HttpResponse(r.text)
            except requests.exceptions.ConnectionError:
                return HttpResponseServerError('与 DreamSpark 服务器通信超时，请稍后重试。')

    if 'error' in request.GET:
        return redirect('http://e5.onthehub.com/d.ashx?s=jlg1p270bi')

    return HttpResponseBadRequest('Bad Request')

def download(request):
    result = get_navbar(request)

    try:
        data = json.loads(open(DATA_ROOT + 'genuine.json').read())
        product = request.GET.get('product', 'windows')

        for navigation in data['navigation']:
            for item in navigation['item']:
                if item['id'] == product:
                    navigation.update({'active': True})
                    break

        items = []
        for software in data['software']:
            if software['id'] == product:
                for edition in software['edition']:
                    edition.update({
                        'channel': {
                            'name': data['channel'][edition['channel']['type']]['name'],
                            'url': data['channel'][edition['channel']['type']]['url'] + edition['channel']['id']
                        }
                })

                items.append(software)

        result.update({'navigation': data['navigation'], 'items': items})
    except IOError:
        pass

    return render_to_response('genuine/download.html', result)
