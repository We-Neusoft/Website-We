# Create your views here.
from django.shortcuts import render_to_response

from markdown import markdown

from www.models import MoreService

def index(request):
    more_services = MoreService.objects.all()
    return render_to_response('www/index.weml', {'nav_www': 'active', 'services': get_services()})

def more_services(request):
    return render_to_response('www/more_services.weml', {'nav_www': 'active', 'services': get_services()})

def get_services():
    services = []

    more_services = MoreService.objects.all().order_by('order')
    for more_service in more_services:
        services.append({
            'key': more_service.key,
            'title': more_service.title,
            'subtitle': more_service.subtitle,
            'content': markdown(more_service.content),
        })

    return services
