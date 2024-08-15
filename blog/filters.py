import django_filters
from .models import Post, Category
from core.models import Tag

class PostFilter(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        field_name='tags',
        to_field_name='id',
    )
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        field_name='category',
        to_field_name='id',
    )
    
    class Meta:
        model = Post
        fields = ['tags', 'category']
