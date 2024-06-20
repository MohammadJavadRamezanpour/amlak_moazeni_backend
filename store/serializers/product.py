from rest_framework import serializers

from store.models import Product
from store.serializers import FileSerializer
from store.serializers.category import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ["price", "rental_price", "title", "text", "status", "category", "files"]
        

class CategoryProductSerializer(serializers.ModelSerializer):
    """
    this is going to be render in categories list
    """
    files = FileSerializer(many=True)

    class Meta:
        model = Product
        fields = ["price", "rental_price", "title", "text", "status", "files"]
