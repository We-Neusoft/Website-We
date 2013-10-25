#coding=utf8
from django.shortcuts import render_to_response

# 首页
def index(request):
    return render_to_response('dreamspark/index.html', {'nav_dreamspark': 'active'})

# 下载
def download(request):
    return render_to_response('dreamspark/download.html', {'nav_dreamspark': 'active'})
