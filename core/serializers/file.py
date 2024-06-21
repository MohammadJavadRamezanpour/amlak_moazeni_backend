from rest_framework import serializers

from core.models import File

class FileSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source="file.url")
    
    class Meta:
        model = File
        fields = ["url", "extension", "mimetype"]
