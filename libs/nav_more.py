from django.core.cache import cache
from django.views import generic

from markdown import markdown

from ip import get_geo
from navigation import get_navbar

from common.models import NavbarItem, NavbarMore
from libs.utils import get_app

class MoreView(generic.ListView):
    template_name = 'common/more.html'
    context_object_name = 'more_list'

    def get_queryset(self):
        return get_more_list(self.request)

    def get_context_data(self, **kwargs):
        context = super(MoreView, self).get_context_data(**kwargs)
        context.update(get_navbar(self.request))
        return context

def get_more_list(request):
    app = NavbarItem.objects.filter(key=get_app(request))
    results = []

    if get_geo(request)[0]:
        more_list = NavbarMore.objects.filter(app=app).filter(intranet=True).order_by('order')
    else:
        more_list = NavbarMore.objects.filter(app=app).filter(internet=True).order_by('order')

    for more in more_list:
        results.append({
            'key': more.key,
            'title': more.title,
            'subtitle': more.subtitle,
            'content': markdown(more.content),
        })

    return results
