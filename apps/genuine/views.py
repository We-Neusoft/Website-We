#encoding=utf8
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render_to_response, redirect
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

import json
import requests
from uuid import UUID

from libs import oauth_client
from navigation import get_navbar

from .models import Catalog, Item

DATA_ROOT = settings.DATA_ROOT

DREAMSPARK_ACCOUNT = settings.DREAMSPARK_ACCOUNT
DREAMSPARK_KEY = settings.DREAMSPARK_KEY

OPEN_LOGIN_REDIRECT_URI = settings.DREAMSPARK_OPEN_REDIRECT_URI

def index(request):
    result = get_navbar(request)

    return render_to_response('genuine/index.html', result)

def iuv(request):
    if 'action' in request.GET:
        action = request.GET['action']

        if request.GET['action'] == 'signin':
            return oauth_client.login(request, OPEN_LOGIN_REDIRECT_URI, ['get_user_email'])

        elif request.GET['action'] == 'signout':
            return redirect('http://e5.onthehub.com/d.ashx?s=jlg1p270bi')

    if 'code' in request.GET:
        code = request.GET['code']

        if oauth_client.get_token(request, OPEN_LOGIN_REDIRECT_URI, code):
            response = json.loads(oauth_client.get_user_email(request))
            if 'email' not in response:
                return oauth_client.login(request, OPEN_LOGIN_REDIRECT_URI, ['get_user_email'])

            email = response['email']
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
            except requests.exceptions.ConnectionError:
                return HttpResponseServerError('与 DreamSpark 服务器通信超时，请稍后重试。')

            if r.status_code == requests.codes.ok:
                return redirect(r.text)
            else:
                return HttpResponse(r.text)

    if 'error' in request.GET:
        return redirect('http://e5.onthehub.com/d.ashx?s=jlg1p270bi')

    return HttpResponseBadRequest('Bad Request')

def download(request):
    result = get_navbar(request)

    # Catalog > Product > Version > Edition > Item
    product = request.GET.get('product', None)
    if product:
        current = Catalog.objects.get(id=UUID(bytes=urlsafe_base64_decode(product)))
    else:
        current = Catalog.objects.filter(name='Windows')[0] # HARD CODING

    catalogs = []
    for catalog in Catalog.objects.filter(parent=None):
        active = False
        products = []
        for product in catalog.catalog_set.all():
            products.append({'name': product.name, 'id': urlsafe_base64_encode(product.id.bytes)})
            if not active and product == current:
                active = True
        catalogs.append({'name': catalog.name, 'products': products, 'active': active})

    result.update({'catalogs': catalogs})

    versions = []
    for version in current.catalog_set.order_by('-order'):
        editions = []
        for edition in version.catalog_set.all():
            items = []
            for item in edition.item_set.all():
                items.append({'name': item.name, 'file': item.file_id})
            editions.append({'name': edition.name, 'items': items})
        versions.append({'id': version.id, 'name': version.name, 'editions': editions})

    result.update({'versions': versions})

    return render_to_response('genuine/download.html', result)
