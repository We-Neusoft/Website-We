#coding=utf-8
from django.contrib import admin

from file.models import File, Download

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'extension', 'size', 'mime', 'created', 'encoded_id', 'file_path', 'download_times')

    def encoded_id(self, obj):
        return obj.id.encode()

    def file_path(self, obj):
        return str(obj.crc32)[-2:] + '/' + obj.md5sum + obj.sha1sum

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
