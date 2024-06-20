from rest_framework import serializers

from store.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()

    def get_products(self, instance):
        from store.serializers.product import CategoryProductSerializer
        products = Product.objects.filter(category=instance)
        return CategoryProductSerializer(products, many=True).data

    def get_image(self, instance):
        return instance.image.url if instance.image else None
    
    class Meta:
        model = Category
        fields = ["image", "title", "text", "products"]
