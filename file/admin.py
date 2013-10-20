#coding=utf-8
from django.contrib import admin

from file.models import File, Download

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'extension', 'size', 'type', 'mime', 'crc32', 'md5sum', 'sha1sum', 'created')

    def has_add_permission(self, request):
        return False
admin.site.register(File, FileAdmin)

class DownloadAdmin(admin.ModelAdmin):
    list_display = ('file', 'ip', 'referer', 'time')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False
admin.site.register(Download, DownloadAdmin)
