from rest_framework import serializers

from core.models import File
from blog.models import Post
from core.serializers import FileSerializer
from .category import CategorySerializer

class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

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
            "tags_list",
        ]


class PostSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()
    category = CategorySerializer()

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
            "tags_list",
            "category",
        ]
