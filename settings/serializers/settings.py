from rest_framework import serializers

from settings.models import Settings

class SettingsSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)

    class Meta:
        model = Settings
        fields = ["phone", "address"]