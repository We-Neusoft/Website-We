#coding=utf8
from django.contrib import admin
from common.models import NavbarItem, NavbarMore

class NavbarItemAdmin(admin.ModelAdmin):
    list_display = ('key', 'title', 'order', 'intranet', 'internet')
admin.site.register(NavbarItem, NavbarItemAdmin)

class NavbarMoreAdmin(admin.ModelAdmin):
    list_display = ('app', 'key', 'title', 'subtitle', 'order', 'intranet', 'internet', 'modified')
    fieldsets = [
        ('属性', {'fields': ['app', 'key', 'order']}),
        ('可见性', {'fields': ['intranet', 'internet']}),
        ('内容', {'fields': ['title', 'subtitle', 'content']}),
    ]
admin.site.register(NavbarMore, NavbarMoreAdmin)
