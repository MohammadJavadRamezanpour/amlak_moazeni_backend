from rest_framework import serializers

from store.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()

    def get_products(self, instance):
        from store.serializers.product import CategoryProductSerializer
        products = Product.objects.filter(category=instance)
        return CategoryProductSerializer(products, many=True, context=self.context).data


    def get_image(self, instance):
        request = self.context.get('request')
        if instance.image is None:
            return None
        if request is not None:
            return request.build_absolute_uri(instance.image.url)
        return instance.image.url
    
    class Meta:
        model = Category
        fields = ["image", "title", "text", "products"]
