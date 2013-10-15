#coding=utf-8
from django.contrib import admin

from file.models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'extension', 'size', 'mime', 'created')
    fieldsets = [
        ('基本信息', {'fields': ['name', 'extension', 'size', 'mime']}),
        ('校验信息', {'fields': ['crc32', 'md5sum', 'sha1sum']}),
    ]
admin.site.register(File, FileAdmin)
