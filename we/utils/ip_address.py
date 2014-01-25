#coding=utf-8
from django.conf import settings

from zlib import crc32

from netaddr import IPAddress, IPNetwork

DEBUG_ENABLED = getattr(settings, 'DEBUG', True)

ip_network = [
    IPNetwork('127.0.0.1/32'),
    IPNetwork('172.18.0.0/16'), IPNetwork('172.19.0.0/17'), IPNetwork('172.21.0.0/17'),
    IPNetwork('172.22.0.0/16'), IPNetwork('172.23.0.0/16'), IPNetwork('172.24.0.0/16'),
    IPNetwork('192.168.24.0/24'), IPNetwork('192.168.102.0/24'),
    IPNetwork('219.216.128.0/24'), IPNetwork('219.216.129.0/27'),
]
ip_name = [
    'localhost',
    'wireless', 'apartment', 'unicom',
    'classroom', 'faculty', 'server_172',
    'administration', 'server_192',
    'server_128', 'server_129',
]

def ipgeo(request):
    address = get_ip(request)

    for network, name in zip(ip_network, ip_name):
        if address in network:
            return name

def get_ip(request):
    if DEBUG_ENABLED:
        return IPAddress(request.META['HTTP_X_REAL_IP'])
    else:
        return IPAddress(request.META['REMOTE_ADDR'])
