import django_filters
from store.models import Product, Category
from core.models import Tag

class ProductFilter(django_filters.FilterSet):
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
        model = Product
        fields = ['tags', 'category']
