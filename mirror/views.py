#coding=utf-8
from django.shortcuts import render_to_response
from os import stat
from time import strftime, localtime

def index(request):
   mirrors = ['apache', 'centos', 'cpan', 'cygwin', 'eclipse', 'epel', 'gentoo', 'putty', 'pypi', 'ubuntu', 'ubuntu-release']
   results = []
   for mirror in mirrors:
      filename = '/storage/mirror/.' + mirror
      result_file = open(filename, 'r')
      result = result_file.readline()[:-1]
      if result == '-1':
         result = '正在同步'
         style = 'we-mirror-syncing'
      elif result == '0':
         result = '同步成功'
         style = 'we-mirror-sync-success'
      else:
         result = '同步失败'
         style = 'we-mirror-sync-faild'
      result_file.close()
      lasttime = stat(filename).st_mtime
      results.append({'mirror': mirror, 'status': result, 'style': style, 'timestamp': strftime('%Y-%m-%d %H:%M:%S', localtime(lasttime))})
   return render_to_response('mirror/index.html', {'results': results})
