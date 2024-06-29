from rest_framework import serializers

from store.models import Product
from core.models import File
from core.serializers import FileSerializer
from store.serializers.category import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()
    category = CategorySerializer()
    thumbnail = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()
    
    def get_thumbnail(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.thumbnail.url)
        return obj.thumbnail.url

    def get_files(self, instance):
        files = File.objects.filter(content_type__model="product", object_id=instance.id)
        return FileSerializer(files, many=True).data

    class Meta:
        model = Product
        fields = ["id", "thumbnail", "price", "rental_price", "title", "text", "status", "category", "files", "created_at"]
        

class CategoryProductSerializer(serializers.ModelSerializer):
    """
    this is going to be render in categories list
    """
    files = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()
    
    def get_thumbnail(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.thumbnail.url)
        return obj.thumbnail.url
    
    def get_files(self, instance):
        files = File.objects.filter(content_type__model="product", object_id=instance.id)
        return FileSerializer(files, many=True, context=self.context).data

    class Meta:
        model = Product
        fields = ["id", "thumbnail", "price", "rental_price", "title", "text", "status", "files", "created_at"]
