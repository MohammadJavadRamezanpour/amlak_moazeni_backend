from rest_framework import serializers

from core.models import File

class FileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ["url", "extension", "mimetype"]

    def get_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.file.url)
        return obj.file.url
