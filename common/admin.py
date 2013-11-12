from django.contrib import admin
from common.models import NavbarItem

class NavbarItemAdmin(admin.ModelAdmin):
    list_display = ('key', 'title', 'order', 'intranet', 'internet')
admin.site.register(NavbarItem, NavbarItemAdmin)
