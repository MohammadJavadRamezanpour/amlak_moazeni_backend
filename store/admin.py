from django.contrib import admin

from store.models import File, Category, Product

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'extension', 'mimetype', 'url']
    readonly_fields = ('extension', 'mimetype')

    def url(self, instance):
        return instance.file.url

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', "rental_price", "status"]
    list_editable = ['price', "rental_price", "status"]