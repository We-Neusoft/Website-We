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
      elif result == 0:
         result = '同步成功'
      else:
         result = '同步失败'
      result_file.close()
      results.append({'mirror': mirror, 'status': result})
   return render_to_response('mirror/index.html', {'results': results})
