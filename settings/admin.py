from django.contrib import admin

from settings.models import Settings, Menues, Slider

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
    
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "text"]
    list_editable = ['title', "text"]
    list_display_links = ["id"]
