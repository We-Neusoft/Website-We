#coding=utf-8
from django.contrib import admin

from file.models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'extension', 'size', 'type', 'mime', 'crc32', 'md5sum', 'sha1sum', 'created')

    def has_add_permission(self, request):
        return False

admin.site.register(File, FileAdmin)
