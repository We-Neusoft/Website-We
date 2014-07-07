from django.conf import settings
from django.shortcuts import render_to_response

import json

from navigation import get_navbar

DATA_ROOT = getattr(settings, 'DATA_ROOT', '/data/www/source')

def index(request):
    result = get_navbar(request)

    return render_to_response('genuine/index.html', result)

def download(request):
    result = get_navbar(request)

    data = json.loads(open(DATA_ROOT + 'genuine.json').read())
    product = request.GET.get('product', 'windows')

    for navigation in data['navigation']:
        for item in navigation['item']:
            if item['id'] == product:
                navigation.update({'active': True})
                break

    items = []
    for software in data['software']:
        if software['id'] == product:
            for edition in software['edition']:
                edition.update({
                    'channel': {
                        'name': data['channel'][edition['channel']['type']]['name'],
                        'url': data['channel'][edition['channel']['type']]['url'] + edition['channel']['id']
                    }
            })

            items.append(software)

    result.update({'navigation': data['navigation'], 'items': items})

    return render_to_response('genuine/download.html', result)
