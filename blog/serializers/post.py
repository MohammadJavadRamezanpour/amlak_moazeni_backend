from rest_framework import serializers

from core.models import File
from blog.models import Post
from core.serializers import FileSerializer
from .category import CategorySerializer
from core.serializers import TagSerializer

class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    # TODO: persian date

    class Meta:
        model = Post
        fields = [
            "id",
            "thumbnail",
            "title",
            "desc",
            "created_at",
            "category",
            "tags",
        ]


class PostSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    def get_files(self, instance):
        files = File.objects.filter(content_type__model="post", object_id=instance.id)
        return FileSerializer(files, many=True).data

    # TODO: persian date

    class Meta:
        model = Post
        fields = [
            "id",
            "thumbnail",
            "title",
            "text",
            "desc",
            "files",
            "created_at",
            "tags",
            "category",
        ]
