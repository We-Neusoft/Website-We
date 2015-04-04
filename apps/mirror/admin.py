from django.contrib import admin

from .models import Mirror, Status

class MirrorAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'active')
admin.site.register(Mirror, MirrorAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('mirror', 'count', 'size', 'time', 'status')
admin.site.register(Status, StatusAdmin)
