from rest_framework import viewset

from store.models import Product
from store.serializers import ProductSerializer

class ReadonlyProductViewset(viewset.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # paginate and filtering
