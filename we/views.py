#encoding=utf-8
from django.views.defaults import page_not_found, server_error

def http_404_view(request):
    response = page_not_found(request)
    response.content += '<hr><p>如果你认为这是一个意外错误，请与我们联系：</p><ul><li>Email: <a href="mailto:we@nou.com.cn">we@nou.com.cn</a><li>QQ 群: 85949649<li>语音信箱: <a href="tel:+8641184756423">+86-411-84756423</a></ul>'

    return response

def http_500_view(request):
    response = server_error(request)
    response.content += '<hr><p>如果你看到此页面，请与我们联系：</p><ul><li>Email: <a href="mailto:we@nou.com.cn">we@nou.com.cn</a><li>QQ 群: 85949649<li>语音信箱: <a href="tel:+8641184756423">+86-411-84756423</a></ul>'

    return response
