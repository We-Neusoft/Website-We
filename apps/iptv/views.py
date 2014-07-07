from django.conf import settings
from django.shortcuts import render_to_response

from datetime import datetime
import csv
import json

from navigation import get_navbar

DATA_ROOT = getattr(settings, 'DATA_ROOT', '/data/www/source/')

def index(request):
    result = get_navbar(request)

    data = json.loads(open(DATA_ROOT + 'tv_channel.json').read())
    result.update({'channels': data})

    return render_to_response('iptv/index.html', result)

def tv(request):
    result = get_navbar(request)

    data = json.loads(open(DATA_ROOT + 'tv_channel.json').read())
    time = json.loads(open(DATA_ROOT + 'tv_time.json').read())

    result.update({'channels': data})

    channel = request.GET.get('channel', 'cctv1')
    for group in data:
        for item in group['channels']:
            if item['channel'] == channel:
                group.update({'active': True})
                result.update({'channel': item})
                break

    for tv in time:
        if tv['channel'] == channel:
            am = []
            pm = []
            for item in tv['list']:
                if datetime.strptime(item['time'], '%H:%M').hour < 12:
                    am.append(item)
                else:
                    pm.append(item)

            result.update({'items': {'am': am, 'pm': pm}})
            break

    return render_to_response('iptv/tv.html', result)

def worldcup(request):
    result = get_navbar(request)

    list = []
    reader = csv.reader(open('/data/www/source/worldcup.csv'))
    for row in reader:
        list.append({'name': row[0], 'id': row[1]})
    result.update({'items': list})

    return render_to_response('iptv/worldcup.html', result)
