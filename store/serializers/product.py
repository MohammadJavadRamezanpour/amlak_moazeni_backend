import jdatetime

from rest_framework import serializers

from store.models import Product, ProductProperty
from core.models import File
from core.serializers import FileSerializer
from store.serializers.category import CategorySerializerWithoutProducts
from store.serializers.product_property import ProductPropertySerializer
from core.serializers import TagSerializer

class ProductSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()
    category = CategorySerializerWithoutProducts()
    thumbnail = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    properties = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)
    created_at = serializers.SerializerMethodField()
    
    def get_created_at(self, instance):
        created_at_gregorian = instance.created_at
        created_at_jalali = jdatetime.datetime.fromgregorian(datetime=created_at_gregorian)
        return created_at_jalali.strftime('%Y/%m/%d')

    def get_properties(self, obj):
        product_properties = ProductProperty.objects.filter(product=obj)
        return ProductPropertySerializer(product_properties, many=True).data

    def get_status(self, obj):
        return obj.get_status_display()

    def get_thumbnail(self, obj):
        request = self.context.get("request")
        if request is not None:
            return request.build_absolute_uri(obj.thumbnail.url)
        return obj.thumbnail.url

    def get_files(self, instance):
        files = File.objects.filter(
            content_type__model="product", object_id=instance.id
        )
        return FileSerializer(files, many=True).data

    class Meta:
        model = Product
        fields = [
            "id",
            "thumbnail",
            "price",
            "rental_price",
            "title",
            "text",
            "status",
            "category",
            "files",
            "created_at",
            "properties",
            "lat",
            "lang",
            "tags"
        ]

class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializerWithoutProducts()
    thumbnail = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    properties = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    
    def get_created_at(self, instance):
        created_at_gregorian = instance.created_at
        created_at_jalali = jdatetime.datetime.fromgregorian(datetime=created_at_gregorian)
        return created_at_jalali.strftime('%Y/%m/%d')

    def get_properties(self, obj):
        product_properties = ProductProperty.objects.filter(product=obj)
        return ProductPropertySerializer(product_properties, many=True).data

    def get_status(self, obj):
        return obj.get_status_display()

    def get_thumbnail(self, obj):
        request = self.context.get("request")
        if request is not None:
            return request.build_absolute_uri(obj.thumbnail.url)
        return obj.thumbnail.url

    class Meta:
        model = Product
        fields = [
            "id",
            "thumbnail",
            "price",
            "rental_price",
            "title",
            "text",
            "status",
            "category",
            "created_at",
            "properties",
            "lat",
            "lang",
        ]

class CategoryProductSerializer(serializers.ModelSerializer):
    """
    this is going to be render in categories list
    """

    files = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    properties = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    
    def get_created_at(self, instance):
        created_at_gregorian = instance.created_at
        created_at_jalali = jdatetime.datetime.fromgregorian(datetime=created_at_gregorian)
        return created_at_jalali.strftime('%Y/%m/%d')

    def get_properties(self, obj):
        product_properties = ProductProperty.objects.filter(product=obj)
        return ProductPropertySerializer(product_properties, many=True).data

    def get_status(self, obj):
        return obj.get_status_display()

    def get_thumbnail(self, obj):
        request = self.context.get("request")
        if request is not None:
            return request.build_absolute_uri(obj.thumbnail.url)
        return obj.thumbnail.url

    def get_files(self, instance):
        files = File.objects.filter(
            content_type__model="product", object_id=instance.id
        )
        return FileSerializer(files, many=True, context=self.context).data

    class Meta:
        model = Product
        fields = [
            "id",
            "thumbnail",
            "price",
            "rental_price",
            "title",
            "text",
            "status",
            "files",
            "created_at",
            "properties",
        ]
