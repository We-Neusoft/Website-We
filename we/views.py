#encoding=utf-8
from django.views.defaults import page_not_found

def http_404_view(request):
    response = page_not_found(request)
    response.content += '<hr><p>如果你认为这是一个意外错误，请与我们联系：</p><ul><li>Email: <a href="mailto:we@nou.com.cn">we@nou.com.cn</a><li>QQ 群: 85949649</ul>'

    return response
