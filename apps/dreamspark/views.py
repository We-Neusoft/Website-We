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
    redirect_uri = 'http://dev.we.neusoft.edu.cn/dreamspark/login.we'

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
        return HttpResponseRedirect(result)
