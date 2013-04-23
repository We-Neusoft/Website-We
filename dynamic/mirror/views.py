#coding=utf-8
import json
import time

from django.shortcuts import render_to_response
from common.unit import file_size

def timestamp_to_localtime(timestamp): 
   return time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(timestamp))

def timestring_to_localtime(timestring): 
   return time.strftime('%Y-%m-%d %H:%M:%S %Z', time.strptime(timestring, '%a %b %d %H:%M:%S %Z %Y'))

def index(request):
   pathname = '/storage/mirror/'
   mirrors = ['centos', 'epel', 'repoforge', 'kali', 'kali-security', 'kali-images', 'linuxmint', 'linuxmint-releases', 'raspbian', 'ubuntu-releases', 'archlinux', 'gentoo', 'gentoo-portage', 'cpan', 'pypi', 'cygwin', 'eclipse', 'putty', 'android', 'qt']
   results = []

   for mirror in mirrors:
      if mirror in ['cpan', 'kali', 'kali-security']:
         status = '实时同步'
         style = 'success'
      else:
         status = open(pathname + '.' + mirror + '.status').readline()[:-1]
         if status == '-1':
            status = '正在同步'
            style = 'info'
         elif status == '0':
            status = '同步成功'
            style = 'success'
         else:
            status = '同步失败'
            style = 'error'

      count = open(pathname + '.' + mirror + '.count').readline()[:-1]
      size = open(pathname + '.' + mirror + '.size').readline()[:-1]

      if mirror == 'cpan':
         timestamp = timestamp_to_localtime(json.loads(open(pathname + mirror + '/RECENT-1h.json').readline())[u'meta'][u'Producers'][u'time'])
      else:
         timestamp = open(pathname + '.' + mirror + '.timestamp').readline()[:-1]

      results.append({'mirror': mirror, 'status': status, 'style': style, 'count': count, 'size': file_size(int(size)), 'timestamp': timestamp})

   return render_to_response('mirror/index.weml', {'nav_mirror': 'active', 'results': results})

def configurations(request):
   return render_to_response('mirror/configurations.weml', {'nav_mirror': 'active'})
