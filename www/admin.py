#coding=utf-8
from django.contrib import admin
from www.models import MoreService

class MoreServiceAdmin(admin.ModelAdmin):
    list_display = ('order', 'key', 'title', 'subtitle', 'modified')
    fieldsets = [
        ('标识', {'fields': ['key', 'order']}),
        ('显示', {'fields': ['intranet', 'internet']}),
        ('标题', {'fields': ['title', 'subtitle']}),
        ('内容', {'fields': ['content']}),
    ]

admin.site.register(MoreService, MoreServiceAdmin)
