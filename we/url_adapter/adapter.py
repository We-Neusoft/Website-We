import re

from django.conf import settings

DEBUG_ENABLED = getattr(settings, 'DEBUG', True)

class AdapterMiddleware(object):
    def process_response(self, request, response):
        self.app = re.match(r'/([^/]+)/', request.path).group(1)

        if DEBUG_ENABLED:
            return response

        response.content = re.sub(r'<a href="/([^/]+)/([^"]+)">', self.handle_href, response.content)

        return response

    def handle_href(self, match):
        target_app = match.group(1)
        target_url = match.group(2)

        return '<a href="' + handle_url(target_app, target_url) + '">'

    def handle_url(self, target_app, target_url):
        if target_app == self.app:
            return '/' + target_url
        else:
            return '://' + target_app + '.we.neusoft.edu.cn/' + target_url
