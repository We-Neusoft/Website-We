#coding=utf-8

from netaddr import IPAddress, IPNetwork

ip_network = [
    IPNetwork('172.18.0.0/16'), IPNetwork('172.19.0.0/17'), IPNetwork('172.21.0.0/17'),
    IPNetwork('172.22.0.0/16'), IPNetwork('172.23.0.0/16'), IPNetwork('172.24.0.0/16'),
    IPNetwork('192.168.24.0/24'), IPNetwork('192.168.102.0/24'),
    IPNetwork('219.216.128.0/24'), IPNetwork('219.216.129.0/27'),
]
ip_name = [
    'wireless', 'apartment', 'unicom',
    'classroom', 'faculty', 'server_172',
    'administration', 'server_192',
    'server_128', 'server_129',
]

def ipgeo(ip):
    address = IPAddress(ip)

    for network, name in zip(ip_network, ip_name):
        if address in network:
            return name
