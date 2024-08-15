from rest_framework import serializers

from blog.models import Category

class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, instance):
        return instance.image.url if instance.image else None
    
    class Meta:
        model = Category
        fields = ["image", "title", "text"]
