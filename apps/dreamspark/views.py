#coding=utf8
from django.conf import settings
from django.contrib.auth import authenticate
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

import json
import urllib, urllib2

from forms import SigninForm, CodeForm
from navigation import get_navbar
from libs import oauth_client

DREAMSPARK_ACCOUNT = getattr(settings, 'DREAMSPARK_ACCOUNT')
DREAMSPARK_KEY = getattr(settings, 'DREAMSPARK_KEY')

OPEN_LOGIN_REDIRECT_URI = getattr(settings, 'DREAMSPARK_OPEN_REDIRECT_URI')

# 首页
def index(request):
    result = get_navbar(request)

    return render_to_response('dreamspark/index.html', result)

# 下载
def download(request):
    result = get_navbar(request)

    return render_to_response('dreamspark/download.html', result)

# 登录
def login(request):
    redirect_uri = OPEN_LOGIN_REDIRECT_URI

    form = CodeForm(request.GET)
    if not form.is_valid():
        response = oauth_client.login(request, redirect_uri)
        if issubclass(response.__class__, HttpResponse):
            return response
    else:
        code = form.cleaned_data['code']
        
        if not oauth_client.get_token(request, redirect_uri, code):
            return HttpResponse('Error')

    token = request.session['token']

    user = oauth_client.get_user_privacy(request, token)
    if user is None:
        request.session.clear()
        return HttpResponseRedirect(redirect_uri)
    else:
        email = json.loads(user)['email']
        domain = email.split('@')[1]
        if domain.lower() == 'nou.com.cn':
            statuses = 'students'
        elif domain.lower() == 'neusoft.edu.cn':
            statuses = 'faculty,staff'

        try:
            result = urllib2.urlopen(
                'https://e5.onthehub.com/WebStore/Security/AuthenticateUser.aspx' +
                '?%s' % urllib.urlencode({
                    'account': DREAMSPARK_ACCOUNT,
                    'key': DREAMSPARK_KEY,
                    'username': email,
                    'academic_statuses': statuses,
                    'email': email,
                }),
            ).read()
        except urllib2.URLError:
            result = '与 DreamSpark 服务器通信超时，请稍后重试。'
        return HttpResponseRedirect(result)
