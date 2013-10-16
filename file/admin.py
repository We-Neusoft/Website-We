#coding=utf-8
from django.contrib import admin

from file.models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'extension', 'size', 'type', 'mime', 'crc32', 'md5sum', 'sha1sum', 'created')

admin.site.register(File, FileAdmin)
