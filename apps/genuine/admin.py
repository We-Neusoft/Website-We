from django.contrib import admin

from .models import Catalog, Item

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'order')
admin.site.register(Catalog, CatalogAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('parent', 'name', 'file_id')
admin.site.register(Item, ItemAdmin)
