from django.contrib import admin

from api.oauth.models import RedirectionUri

class RedirectionUriAdmin(admin.ModelAdmin):
    list_display = ('client', 'uri')

admin.site.register(RedirectionUri, RedirectionUriAdmin)
