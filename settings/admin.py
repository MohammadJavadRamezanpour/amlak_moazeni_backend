from django.contrib import admin

from settings.models import Settings, Menues, Slider

# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'address']
    list_editable = ['phone', "address"]
    list_display_links = ["id"]


@admin.register(Menues)
class MenuesAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', "link", "active", "is_root"]
    list_editable = ['text', "active"]
    list_display_links = ["id"]

    def is_root(self, instance):
        return instance.parent is None
    is_root.boolean = True
    
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "text"]
    list_editable = ['title', "text"]
    list_display_links = ["id"]
