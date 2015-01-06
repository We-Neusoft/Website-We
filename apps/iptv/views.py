from django.conf import settings
from django.shortcuts import render_to_response

from datetime import datetime
from os.path import isfile
import csv
import json

from navigation import get_navbar

DATA_ROOT = getattr(settings, 'DATA_ROOT', '/data/www/source/')
SCREENSHOT_ROOT = getattr(settings, 'SCREENSHOT_ROOT', '/data/www/we/iptv/screenshots/')

def index(request):
    result = get_navbar(request)
    get_active_channel(result)

    return render_to_response('iptv/index.html', result)

def tv(request):
    result = get_navbar(request)
    get_active_channel(result)

    channel = request.GET.get('channel', 'CCTV-1')
    for group in result['channels']:
        for item in group['channels']:
            if item['channel'] == channel:
                group.update({'active': True})
                result.update({'channel': item})
                break

    all_list = json.loads(open(DATA_ROOT + 'tv_time.json').read())
    for item in all_list:
        if item['channel'] == channel:
            list = item['list']

            am = []
            pm = []
            for item in list:
                if datetime.strptime(item['time'], '%H:%M').time().hour < 12:
                    am.append(item)
                else:
                    pm.append(item)

            playing = 0
            for index in range(len(list)):
                current = datetime.strptime(list[index]['time'], '%H:%M').time()
                now = datetime.now().time()

                if (now < current):
                    break
                else:
                    playing = index

            if playing < len(am):
                am[playing].update({'current': True})
            else:
                pm[playing - len(am)].update({'current': True})

            result.update({'items': {'am': am, 'pm': pm}})

    return render_to_response('iptv/tv.html', result)

def get_active_channel(result):
    data = json.loads(open(DATA_ROOT + 'tv_channel.json').read())
    for group in data[:]:
        for channel in group['channels'][:]:
            for point in channel['point'][:]:
                if not isfile(SCREENSHOT_ROOT + point['point'] + '.png'):
                    channel['point'].remove(point)
            if not channel['point']:
                group['channels'].remove(channel)
        if not group['channels']:
            data.remove(group)

    result.update({'channels': data})

def voice_of_china(request):
    result = get_navbar(request)

    list = []
    reader = csv.reader(open(DATA_ROOT + 'voice_of_china.csv'))
    for row in reader:
        list.append({'name': row[0], 'id': row[1]})
    result.update({'items': list})
    
    return render_to_response('iptv/voice_of_china.html', result)

def voice_of_china_2014(request):
    result = get_navbar(request)

    return render_to_response('iptv/voice_of_china_2014.html', result)

def worldcup_2014(request):
    result = get_navbar(request)

    return render_to_response('iptv/worldcup_2014.html', result)
