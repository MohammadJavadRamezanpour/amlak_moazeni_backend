from django.contrib import admin

from settings.models import Settings, Menues

# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'address']
    list_editable = ['phone', "address"]
    list_display_links = ["id"]


@admin.register(Menues)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', "link", "active"]
    list_editable = ['text', "active"]
    list_display_links = ["id"]
    
