from rest_framework import serializers

from settings.models import Settings


class BaseSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Settings
        fields = ["phone", "address"]


class SettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Settings
        fields = ["phone", "address", "intro_image", "intro_header", "intro_text"]

class IntroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Settings
        fields = ["intro_image", "intro_header", "intro_text"]
