from rest_framework import serializers

from store.models import  ProductProperty

class ProductPropertySerializer(serializers.ModelSerializer):
    icon = serializers.CharField(source='property.icon')
    title = serializers.CharField(source='property.title')

    class Meta:
        model = ProductProperty
        fields = ['icon', 'title', 'value']
