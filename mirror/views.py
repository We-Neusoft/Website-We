#coding=utf-8
from django.shortcuts import render_to_response

def index(request):
   mirrors = ['centos', 'epel', 'ubuntu', 'ubuntu-releases', 'gentoo', 'cpan', 'pypi', 'apache', 'cygwin', 'eclipse', 'putty']
   results = []
   for mirror in mirrors:
      pathname = '/storage/mirror/'
      status = open(pathname + '.' + mirror + '.status').readline()[:-1]
      if status == '-1':
         status = '正在同步'
         style = 'we-mirror-syncing'
      elif status == '0':
         status = '同步成功'
         style = 'we-mirror-sync-success'
      else:
         status = '同步失败'
         style = 'we-mirror-sync-faild'
      timestamp = open(pathname + '.' + mirror + '.timestamp').readline()[:-1]
      results.append({'mirror': mirror, 'status': status, 'style': style, 'timestamp': timestamp})
   return render_to_response('mirror/index.html', {'results': results})
