#coding=utf-8
from django.core.cache import cache
from django.core.urlresolvers import resolve, reverse

from common.models import NavbarItem
from we.utils.ipgeo import ipgeo

def get_navbar(request):
    if ipgeo(request):
        items = cache.get('navbar_items__intranet')
        if not items:
            items = NavbarItem.objects.filter(intranet=True).order_by('order')
            cache.set('navbar_items__intranet', items, 600)
    else:
        items = cache.get('navbar_items__internet')
        if not items:
            items = NavbarItem.objects.filter(internet=True).order_by('order')
            cache.set('navbar_items__internet', items, 600)

    navbar_items = []
    for item in items:
        navbar_items.append({'key': item.key, 'title': item.title, 'url': reverse(item.key + ':index')})

    result = dict()
    result.update({'navbar_items': navbar_items})
    result.update({'active_item': resolve(request.path).namespace})

    return result

def get_username(request):
    return {'username': get_name(request), 'is_logged': request.user.is_authenticated()}

def get_name(request):
    if request.user.is_authenticated():
        try:
            return request.user.profile.nickname
        except:
            return request.user.username
    else:
        address = ipgeo(request)
        if not address:
            return '访客'
        elif address in ['faculty', 'administration']:
            return '老师'
        elif address[:6] == 'server':
            return '朋友'
        else:
            return '同学'
