#coding=utf-8
from django.shortcuts import render_to_response

from navigation import get_navbar
from converter import file_size

from .models import Mirror, Status
from libs.nav_more import MoreView, get_more_list

pathname = '/storage/mirror/'

# 首页
def index(request):
    result = get_navbar(request)
    result.update({'more_list': get_more_list(request)})

    results = []
    mirrors = Mirror.objects.filter(active=True).order_by('order')
    for mirror in mirrors:
        item = mirror.status

        try:
            if mirror.name in ['cpan']:
                item.status = '实时同步'
                item.style = 'success'
            elif mirror.name in ['kali', 'kali-security']:
                item.status = '被动同步'
                item.style = 'success'
            else:
                if item.status == -1:
                    item.status = '正在同步'
                    item.style = 'info'
                elif item.status == -2:
                    item.status = '正在统计'
                    item.style = 'info'
                elif item.status == 0:
                    item.status = '同步成功'
                    item.style = 'success'
                elif item.status is None:
                    item.status = '状态未知'
                    item.style = 'default'
                else:
                    item.status = '同步失败'
                    item.style = 'danger'

            results.append({
                'mirror': mirror.name, 'status': item.status, 'style': item.style, 'count': item.count, 'size': file_size(item.size), 'timestamp': item.time
            })
        except Status.DoesNotExist:
            pass

    result.update({'results': results})

    return render_to_response('mirror/index.html', result)

class MoreView(MoreView):
    def get_context_data(self, **kwargs):
        context = super(MoreView, self).get_context_data(**kwargs)
        context.update({
            'more_title': '配置说明 - 开源镜像站',
            'more_dropdown': '配置说明',
        })
        return context