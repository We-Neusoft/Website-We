#coding=utf-8

from we.utils.ipgeo import ipgeo

def get_username(request):
    return {'username': get_name(request)}

def get_name(request):
    if request.user.is_authenticated():
        return request.user.username
    else:
        address = ipgeo(request.META['REMOTE_ADDR'])
        if not address:
            return '访客'
        elif address == 'faculty':
            return '老师'
        elif address[:6] == 'server':
            return '朋友'
        else:
            return '同学'
