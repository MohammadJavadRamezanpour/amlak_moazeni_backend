from django.contrib import admin
from blog.models import Post, Category
from django.db import models
from ckeditor.widgets import CKEditorWidget

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at", "publish"]
    list_editable = ["title", "publish"]
    list_filter = ["publish", "created_at"]
    search_fields = ["title"]
    readonly_fields = ["created_at"]
    formfield_overrides = {
        "text": {'widget': CKEditorWidget()},
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_editable = ["title"]
    search_fields = ["title"]
