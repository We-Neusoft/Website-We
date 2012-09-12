#coding=utf-8
from django.shortcuts import render_to_response
from common.unit import file_size

def index(request):
   mirrors = ['centos', 'epel', 'repoforge', 'ubuntu', 'ubuntu-releases', 'archlinux', 'gentoo', 'gentoo-portage', 'cpan', 'pypi', 'apache', 'cygwin', 'eclipse', 'mozilla-current', 'putty']
   results = []
   for mirror in mirrors:
      pathname = '/storage/mirror/'
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
      size = open(pathname + '.' + mirror + '.size').readline()[:-1]
      count = open(pathname + '.' + mirror + '.count').readline()[:-1]
      timestamp = open(pathname + '.' + mirror + '.timestamp').readline()[:-1]
      results.append({'mirror': mirror, 'status': status, 'style': style, 'size': file_size(int(size)), 'count': count, 'timestamp': timestamp})
   return render_to_response('mirror/index.weml', {'results': results})
