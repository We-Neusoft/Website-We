#coding=utf8
from django.conf import settings
from django.contrib.auth import authenticate
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from we.utils.auth import get_username
from dreamspark.forms import SigninForm

from httplib import HTTPSConnection

DREAMSPARK_ACCOUNT = getattr(settings, 'DREAMSPARK_ACCOUNT')
DREAMSPARK_KEY = getattr(settings, 'DREAMSPARK_KEY')

# 首页
def index(request):
    result = get_username(request)
    result.update({'nav_dreamspark': 'active'})

    return render_to_response('dreamspark/index.html', result)

# 下载
def download(request):
    result = get_username(request)
    result.update({'nav_dreamspark': 'active'})

    return render_to_response('dreamspark/download.html', result)

# 登录
def signin(request):
    result = get_username(request)
    result.update({'nav_dreamspark': 'active'})

    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            domain = form.cleaned_data['domain']
            password = form.cleaned_data['password']

            user = authenticate(username=username, domain=domain, password=password)

            if user:
                try:
                    onthehub = HTTPSConnection('e5.onthehub.com')
                    onthehub.request('GET', '/WebStore/Security/AuthenticateUser.aspx?account=' + DREAMSPARK_ACCOUNT + '&username=' + user.username + '&key=' + DREAMSPARK_KEY + '&academic_statuses=' + ('students' if domain == '@nou.com.cn' else 'faculty,staff') + '&email=' + user.email + '&last_name=' + user.last_name + '&first_name=' + user.first_name)
                    response = onthehub.getresponse()
                    if response.status == 200:
                        return HttpResponseRedirect(response.read())
                    else:
                        result.update({'error': '与 DreamSpark 通信异常，请稍后重试'})
                except:
                    result.update({'error': '与 DreamSpark 通信超时，请稍后重试'})
            else:
                result.update({'error': '邮箱地址或密码错误，请重新输入'})

    result.update(csrf(request))

    return render_to_response('dreamspark/signin.html', result)
