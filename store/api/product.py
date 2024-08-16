from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from store.models import Product
from store.serializers import ProductSerializer, ProductListSerializer
from core.misc import CustomPaginationClass
from store.filters import ProductFilter


class ProductViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPaginationClass      
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'tags__text']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        return ProductSerializer
