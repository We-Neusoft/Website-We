#coding=utf-8
import json
import memcache
import time

from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page

from we.utils.unit import file_size

pathname = '/storage/mirror/'
memcached = memcache.Client(['127.0.0.1:11211'], debug=0)

# 首页
def index(request):
    mirrors = ['centos', 'epel', 'repoforge', 'kali', 'kali-security', 'kali-images', 'linuxmint', 'linuxmint-releases', 'raspbian', 'ubuntu-releases', 'archlinux', 'gentoo', 'gentoo-portage', 'cpan', 'pypi', 'rubygems', 'cygwin', 'eclipse', 'putty', 'android', 'qt', 'ldp']
    results = []

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

        results.append({'mirror': mirror, 'status': status, 'style': style, 'count': count, 'size': file_size(int(size)), 'timestamp': timestamp})

    return render_to_response('mirror/index.weml', {'nav_mirror': 'active', 'results': results})

# 配置说明
def configurations(request):
    return render_to_response('mirror/configurations.weml', {'nav_mirror': 'active'})

# 从memcache中获得数据
def get_value(mirror, key, time=0):
    if (mirror == 'cpan' and key == 'timestamp'):
        return timestamp_to_localtime(json.loads(open(pathname + mirror + '/RECENT-1h.json').readline())[u'meta'][u'Producers'][u'time'])

    value = memcached.get(mirror + '_' + key)
    if not value:
        value = open(pathname + '.' + mirror + '.' + key).readline()[:-1]
        memcached.set(mirror + '_' + key, value, time)

    return value

# 将timestamp转换成本地时间
def timestamp_to_localtime(timestamp): 
    return time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(timestamp))
