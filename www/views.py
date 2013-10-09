#coding=utf-8
from django.shortcuts import render_to_response

from markdown import markdown

from www.models import MoreService

# 首页
def index(request):
    return render_to_response('www/index.weml', {'nav_www': 'active', 'services': get_services()})

# 更多服务
def more_services(request):
    return render_to_response('www/more_services.weml', {'nav_www': 'active', 'services': get_services()})

# 获得更多服务列表
def get_services():
    services = []

    more_services = MoreService.objects.filter(intranet=True).order_by('order')
    for more_service in more_services:
        services.append({
            'key': more_service.key,
            'title': more_service.title,
            'subtitle': more_service.subtitle,
            'content': markdown(more_service.content),
        })

    return services
