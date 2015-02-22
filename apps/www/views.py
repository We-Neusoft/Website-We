#encoding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response

from navigation import get_navbar

from libs.nav_more import MoreView, get_more_list

def index(request):
    result = get_navbar(request)
    result.update({'more_list': get_more_list(request)})

    return render_to_response('www/index.html', result)

class MoreView(MoreView):
    def get_context_data(self, **kwargs):
        context = super(MoreView, self).get_context_data(**kwargs)
        context.update({
            'more_title': '更多服务 - 首页',
            'more_dropdown': '更多服务',
        })
        return context