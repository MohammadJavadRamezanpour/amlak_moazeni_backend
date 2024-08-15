from django.contrib import admin
from core.models import File, Tag

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'extension', 'mimetype', 'url']
    readonly_fields = ('extension', 'mimetype')

    def url(self, instance):
        return instance.file.url
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['text']
