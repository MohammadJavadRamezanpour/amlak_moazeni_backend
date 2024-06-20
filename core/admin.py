from django.contrib import admin
from core.models import File

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'extension', 'mimetype', 'url']
    readonly_fields = ('extension', 'mimetype')

    def url(self, instance):
        return instance.file.url
