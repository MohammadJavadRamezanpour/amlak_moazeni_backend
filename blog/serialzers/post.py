from rest_framework import serializers

from core.models import File
from blog.models import Post
from core.serializers import FileSerializer

class PostSerializer(serializers.ModelSerializer):
    files = serializers.SerializerMethodField()

    def get_files(self, instance):
        files = File.objects.filter(content_type__model="post", object_id=instance.id)
        return FileSerializer(files, many=True).data

    class Meta:
        model = Post
        fields = ["id", "thumbnail", "title", "text", "files", "created_at"]
        