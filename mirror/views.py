#coding=utf-8
from django.shortcuts import render_to_response

def index(request):
   mirrors = ['apache', 'centos', 'cpan', 'cygwin', 'eclipse', 'epel', 'gentoo', 'putty', 'putty', 'pypi', 'ubuntu', 'ubuntu-release']
   results = []
   for mirror in mirrors:
      result_file = open('/storage/mirror/.' + mirror, 'r')
      result = result_file.read()
      if result < 0:
         result = '同步中...'
         style = 'we-mirror-syncing'
      elif result == 0:
         result = '同步成功'
         style = 'we-mirror-sync-success'
      else:
         result = '同步失败'
         style = 'we-mirror-sync-faild'
      result_file.close()
      results.append({'mirror': mirror, 'status': result, 'style': style})
   return render_to_response('mirror/index.html', {'results': results})
