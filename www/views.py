#coding=utf-8
from django.shortcuts import render_to_response
from django.views import generic

from we.utils.navbar import get_navbar
from www.models import MoreService

from markdown import markdown

# 首页
def index(request):
    result = get_navbar(request)
    result.update({'active_item': 'www'})
    result.update({'more_service_list': get_services()})

    return render_to_response('www/index.html', result)

# 更多服务
class MoreServicesView(generic.ListView):
    template_name = 'www/more_services.html'
    context_object_name = 'more_service_list'

    def get_queryset(self):
        return get_services()

    def get_context_data(self, **kwargs):
        context = super(MoreServicesView, self).get_context_data(**kwargs)
        context.update(get_navbar(self.request))
        context.update({'nav_www': 'active'})
        return context

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
