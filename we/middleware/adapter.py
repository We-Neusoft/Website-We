from django.conf import settings
from django.core.urlresolvers import resolve, Resolver404
from django.http import HttpResponseNotFound

import re

from ip import get_geo

DEBUG_ENABLED = getattr(settings, 'DEBUG', True)

class AdapterMiddleware(object):
    def process_response(self, request, response):
        try:
            self.app = resolve(request.path).namespace
        except Resolver404:
            return response

        if DEBUG_ENABLED:
            return response
        if response.has_header('location'):
            if response['location'].startswith('/'):
                response['location'] = re.sub(r'/([^/]+)(.*)', self.handle_location, response['location'])
            elif response['location'].startswith('http://hub.neusoft.edu.cn/'):
                response['location'] = re.sub(r'http://hub.neusoft.edu.cn/([^/]+)(.*)', self.handle_hub, response['location'])
            return response
        if not hasattr(response, 'content'):
            return response

        response.content = re.sub(r'http://hub.neusoft.edu.cn/([^/]+)([^"]+)', self.handle_hub, response.content)
        response.content = re.sub(r'<link([^>]*)href="/([^"]*)"([^>]*)>', self.handle_link, response.content)
        response.content = re.sub(r'<script([^>]*)src="/([^"]*)"([^>]*)>', self.handle_script, response.content)
        response.content = re.sub(r'<a([^>]*)href="/([^/]+)([^"]*)"([^>]*)>', self.handle_a, response.content)
        response.content = re.sub(r'<form([^>]*)action="/([^/]+)([^"]*)"([^>]*)>', self.handle_form, response.content)
        response.content = re.sub(r'<img([^>]*)src="/([^/]+)([^"]*)"([^>]*)>', self.handle_img, response.content)

        response.content = re.sub('iptv.we.neusoft.edu.cn', 'iptv.neusoft.edu.cn', response.content)
        if not get_geo(request)[0]:
            response.content = re.sub('mirror.we.neusoft.edu.cn', 'mirrors.neusoft.edu.cn', response.content)

        return response

    def handle_location(self, match):
        target_app = match.group(1)
        target_url = match.group(2)

        return self.handle_url(target_app, target_url)

    def handle_hub(self, match):
        target_app = match.group(1)
        target_url = match.group(2)

        return '//' + target_app + '.hub.neusoft.edu.cn' + target_url

    def handle_link(self, match):
        target_url = match.group(2)
        property_pre = match.group(1)
        property_suf = match.group(3)

        return '<link' + property_pre + 'href="/' + target_url + '"' + property_suf + '>'

    def handle_script(self, match):
        target_url = match.group(2)
        property_pre = match.group(1)
        property_suf = match.group(3)

        return '<script' + property_pre + 'src="/' + target_url + '"' + property_suf + '>'

    def handle_a(self, match):
        target_app = match.group(2)
        target_url = match.group(3)
        property_pre = match.group(1)
        property_suf = match.group(4)

        return '<a' + property_pre + 'href="' + self.handle_url(target_app, target_url) + '"' + property_suf + '>'

    def handle_form(self, match):
        target_app = match.group(2)
        target_url = match.group(3)
        property_pre = match.group(1)
        property_suf = match.group(4)

        return '<form' + property_pre + 'action="' + self.handle_url(target_app, target_url) + '"' + property_suf + '>'

    def handle_img(self, match):
        target_app = match.group(2)
        target_url = match.group(3)
        property_pre = match.group(1)
        property_suf = match.group(4)

        return '<img' + property_pre + 'src="' + self.handle_url(target_app, target_url) + '"' + property_suf + '>'

    def handle_url(self, target_app, target_url):
        if target_app == 'admin':
            return '/' + target_app + target_url
        elif target_app == 'static':
            return '/' + target_app + target_url
        elif target_app == self.app:
            return target_url
        else:
            return '//' + self.handle_domain(target_app) + target_url

    def handle_domain(self, target_app):
        if target_app == 'www':
            return 'we.neusoft.edu.cn'
        else:
            return target_app + '.we.neusoft.edu.cn'
