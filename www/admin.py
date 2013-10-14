#coding=utf-8
from django.contrib import admin
from www.models import MoreService

class MoreServiceAdmin(admin.ModelAdmin):
    list_display = ('key', 'title', 'subtitle', 'order', 'intranet', 'internet', 'modified')
    fieldsets = [
        ('属性', {'fields': ['key', 'order']}),
        ('可见性', {'fields': ['intranet', 'internet']}),
        ('内容', {'fields': ['title', 'subtitle', 'content']}),
    ]

admin.site.register(MoreService, MoreServiceAdmin)
