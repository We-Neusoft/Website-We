from django.contrib import admin

from models import Url

class UrlAdmin(admin.ModelAdmin):
    list_display = ('url', )

admin.site.register(Url, UrlAdmin)
