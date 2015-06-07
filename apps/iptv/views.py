from django.shortcuts import render_to_response, get_object_or_404

from .models import Group, Channel, Guide

from datetime import datetime, time
from os.path import isfile
import csv
import json

from navigation import get_navbar

def index(request):
    result = get_navbar(request)
    get_active_channel(result)

    return render_to_response('iptv/index.html', result)

def tv(request):
    result = get_navbar(request)
    get_active_channel(result)

    channel = get_object_or_404(Channel, channel=request.GET.get('channel', 'CCTV-1'))
    for group in result['channels']:
        for item in group['channels']:
            if item['channel'] == channel.channel:
                group.update({'active': True})
                result.update({'channel': item})
                break

    guide = Guide.objects.filter(channel=channel)

    noon = time(12)
    am = guide.filter(time__lt=noon)
    pm = guide.filter(time__gte=noon)
    result.update({'items': {'am': am, 'pm': pm}})

    now = datetime.now().time()
    index = guide.filter(time__lt=now).count() - 1
    if index < len(am):
        result.update({'current': {'am': index}})
    else:
        result.update({'current': {'pm': index - len(am)}})

    return render_to_response('iptv/tv.html', result)

def get_active_channel(result):
    groups = Group.objects.all()

    data = []
    for group in groups:
        channels = []
        for channel in group.channel_set.all():
            points = []
            for point in channel.point_set.filter(active=True):
                points.append(point)
            if points:
                channels.append({'name': channel.name, 'channel': channel.channel, 'point': points, 'hd': points[0].hd})
        if channels:
            data.append({'name': group.name, 'channels': channels})

    result.update({'channels': data})

def voice_of_china_2014(request):
    result = get_navbar(request)

    return render_to_response('iptv/voice_of_china_2014.html', result)

def worldcup_2014(request):
    result = get_navbar(request)

    return render_to_response('iptv/worldcup_2014.html', result)
