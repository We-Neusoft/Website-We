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
   mirrors = ['centos', 'epel', 'repoforge', 'ubuntu', 'ubuntu-releases', 'archlinux', 'gentoo', 'gentoo-portage', 'cpan', 'apache', 'cygwin', 'eclipse', 'mozilla-current', 'putty']
   results = []

   for mirror in mirrors:
      if mirror == 'cpan':
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

      if mirror == 'centos':
         timestamp = timestamp_to_localtime(int(open(pathname + mirror + '/TIME').readline()))
      elif mirror == 'cpan':
         timestamp = timestamp_to_localtime(json.loads(open(pathname + mirror + '/RECENT-1h.json').readline())[u'meta'][u'Producers'][u'time'])
      elif mirror == 'repoforge':
         timestamp = timestamp_to_localtime(int(open(pathname + mirror + '/TIME').readline()))
      elif mirror == 'ubuntu':
         timestamp = timestring_to_localtime(open(pathname + mirror + '/project/trace/sadashbia.canonical.com').readline()[:-1])
      elif mirror == 'archlinux':
         timestamp = timestamp_to_localtime(int(open(pathname + mirror + '/lastsync').readline()))
      elif mirror == 'gentoo':
         timestamp = timestamp_to_localtime(int(open(pathname + mirror + '/experimental/timestamp.mirmon').readline()))
      elif mirror == 'apache':
         timestamp = timestamp_to_localtime(int(open(pathname + mirror + '/zzz/time.txt').readline()))
      elif mirror == 'eclipse':
         timestamp = timestamp_to_localtime(int(open(pathname + mirror + '/TIME').readline()))
#      elif mirror == 'mozilla-current':
#         timestamp = timestring_to_localtime(open(pathname + mirror + '/zz/marker.txt').readline()[:-1])
      else:
         timestamp = open(pathname + '.' + mirror + '.timestamp').readline()[:-1]

      results.append({'mirror': mirror, 'status': status, 'style': style, 'count': count, 'size': file_size(int(size)), 'timestamp': timestamp})

   return render_to_response('mirror/index.weml', {'results': results})
