from django.contrib import admin

from .models import Group, Channel, Point, Guide

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
admin.site.register(Group, GroupAdmin)

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'order')
admin.site.register(Channel, ChannelAdmin)

class PointAdmin(admin.ModelAdmin):
    list_display = ('channel', 'source', 'target', 'hd', 'active')
admin.site.register(Point, PointAdmin)

class GuideAdmin(admin.ModelAdmin):
    list_display = ('channel', 'time', 'name')
admin.site.register(Guide, GuideAdmin)
