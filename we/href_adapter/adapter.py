from django.conf import settings

import re

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
        target_href = match.group(2)

        if target_app == self.app:
            result_href = '/' + target_href
        else:
            result_href = '://' + target_app + '.we.neusoft.edu.cn/' + target_href

        return '<a href="' + result_href + '">'
