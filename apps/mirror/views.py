#coding=utf-8
from django.core.cache import cache
from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page

import json
import time

from navigation import get_navbar
from converter import file_size

pathname = '/storage/mirror/'

# 首页
def index(request):
    result = get_navbar(request)

    results = []
    mirrors = ['centos', 'epel', 'atomic', 'repoforge', 'kali', 'kali-security', 'kali-images', 'raspbian', 'ubuntu-releases', 'archlinux', 'gentoo', 'gentoo-portage', 'mariadb', 'cpan', 'pypi', 'rubygems', 'cygwin', 'eclipse', 'putty', 'android', 'qt', 'ldp', 'lfs', 'blfs']
    for mirror in mirrors:
        if mirror in ['cpan', 'kali', 'kali-security']:
            status = '实时同步'
            style = 'success'
        else:
            status = get_value(mirror, 'status')

            if status == '-1':
                status = '正在同步'
                style = 'info'
            elif status == '0':
                status = '同步成功'
                style = 'success'
            else:
                status = '同步失败'
                style = 'error'

        count = get_value(mirror, 'count')
        size = get_value(mirror, 'size')
        timestamp = get_value(mirror, 'timestamp')

        results.append({
            'mirror': mirror, 'status': status, 'style': style, 'count': count, 'size': file_size(int(size)), 'timestamp': timestamp
        })
    result.update({'results': results})

    return render_to_response('mirror/index.html', result)

# 配置说明
def configurations(request):
    result = get_navbar(request)
    return render_to_response('mirror/configurations.html', result)

# 从cache中获得数据
def get_value(mirror, key, time=0):
    if (mirror == 'cpan' and key == 'timestamp'):
        return timestamp_to_localtime(json.loads(open(pathname + mirror + '/RECENT-1h.json').readline())[u'meta'][u'Producers'][u'time'])

    value = cache.get(mirror + '_' + key)
    if not value:
        value = open(pathname + '.' + mirror + '.' + key).readline()[:-1]
        cache.set(mirror + '_' + key, value, time)

    return value

# 将timestamp转换成本地时间
def timestamp_to_localtime(timestamp): 
    return time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(timestamp))
