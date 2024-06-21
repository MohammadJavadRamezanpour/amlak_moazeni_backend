from django.contrib import admin

from store.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', "rental_price", "status"]
    list_editable = ['price', "rental_price", "status"]
    list_filter = ["status"]
    search_fields = ["title"]
    readonly_fields = ["created_at"]

