import re

from django.conf import settings

DEBUG_ENABLED = getattr(settings, 'DEBUG', True)

class AdapterMiddleware(object):
    def process_response(self, request, response):
        self.app = re.match(r'/([^/]+)/', request.path).group(1)

        if DEBUG_ENABLED:
            return response

        response.content = re.sub(r'<a href="/([^/]+)/([^"]*)">', self.handle_a, response.content)
        response.content = re.sub(r'<form(([^>]*)action="/([^/]+)/([^"]*)"([^>]*))>', self.handle_form, response.content)

        return response

    def handle_a(self, match):
        target_app = match.group(1)
        target_url = match.group(2)

        return '<a href="' + self.handle_url(target_app, target_url) + '">'

    def handle_form(self, match):
        target_app = match.group(3)
        target_url = match.group(4)
        property_pre = match.group(2)
        property_suf = match.group(5)

        return '<form' + property_pre + 'action="' + self.handle_url(target_app, target_url) + '"' + property_suf + '>'

    def handle_url(self, target_app, target_url):
        if target_app == self.app:
            return '/' + target_url
        else:
            return '//' + self.handle_domain(target_app) + '/' + target_url

    def handle_domain(self, target_app):
        if target_app == 'www':
            return 'we.neusoft.edu.cn'
        elif target_app == 'mirror':
            return 'mirrors.neusoft.edu.cn'
        else:
            return target_app + '.we.neusoft.edu.cn'
