#coding=utf-8
from django.contrib import admin

from .models import File, Download

from converter import uuid_encode

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'extension', 'size', 'mime', 'created', 'encoded_id', 'file_path', 'download_times')

    def encoded_id(self, obj):
        return uuid_encode(obj.id)

    def file_path(self, obj):
        return str(obj.crc32)[-2:] + '/' + obj.md5sum + obj.sha1sum

    def has_add_permission(self, request, obj=None):
        return False
admin.site.register(File, FileAdmin)

class DownloadAdmin(admin.ModelAdmin):
    list_display = ('file', 'ip', 'referer', 'time')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(Download, DownloadAdmin)
