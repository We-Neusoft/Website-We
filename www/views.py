#coding=utf-8
from django.shortcuts import render_to_response
from django.views import generic

from markdown import markdown

from www.models import MoreService

# 首页
def index(request):
    return render_to_response('www/index.html', {'nav_www': 'active', 'services': get_services()})

# 更多服务
class MoreServicesView(generic.ListView):
    template_name = 'www/more_services.html'
    context_object_name = 'more_service_list'

    def get_queryset(self):
        return get_services()

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
