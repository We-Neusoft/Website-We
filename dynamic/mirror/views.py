#coding=utf-8
import json
import time

from django.shortcuts import render_to_response
from common.unit import file_size

def index(request):
   mirrors = ['centos', 'epel', 'repoforge', 'ubuntu', 'ubuntu-releases', 'archlinux', 'gentoo', 'gentoo-portage', 'cpan', 'apache', 'cygwin', 'eclipse', 'mozilla-current', 'putty']
   results = []
   for mirror in mirrors:
      pathname = '/storage/mirror/'
      if mirror == 'cpan':
         status = '实时同步'
         style = 'success'
         timestamp = time.strftime('%Y-%m-%d %H-%M-%S %Z', time.localtime(json.loads(open(pathname + 'cpan/RECENT-1h.json').readline())[u'meta'][u'Producers'][u'time']))
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
         timestamp = open(pathname + '.' + mirror + '.timestamp').readline()[:-1]
      count = open(pathname + '.' + mirror + '.count').readline()[:-1]
      size = open(pathname + '.' + mirror + '.size').readline()[:-1]
      results.append({'mirror': mirror, 'status': status, 'style': style, 'count': count, 'size': file_size(int(size)), 'timestamp': timestamp})
   return render_to_response('mirror/index.weml', {'results': results})
