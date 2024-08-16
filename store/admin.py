from django.contrib import admin

from store.models import Category, Product, Property, ProductProperty


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text']

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title')

@admin.register(ProductProperty)
class ProductPropertyAdmin(admin.ModelAdmin):
    list_display = ('product', 'property', 'value')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', "rental_price", "status", "category"]
    list_editable = ['price', "rental_price", "status"]
    list_filter = ["status", "category"]
    search_fields = ["title"]
    readonly_fields = ["created_at"]

    def category(self, instance):
        return instance.category.title
