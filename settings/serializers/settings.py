from rest_framework import serializers

from settings.models import Settings


class BaseSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Settings
        fields = ["phone", "address"]


class SettingsSerializer(serializers.ModelSerializer):
    intro_image = serializers.SerializerMethodField()

    class Meta:
        model = Settings
        fields = ["phone", "address", "intro_image", "intro_header", "intro_text"]

    def get_intro_image(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.intro_image.url)
        return obj.intro_image.url

class IntroSerializer(serializers.ModelSerializer):
    intro_image = serializers.SerializerMethodField()
    
    def get_intro_image(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.intro_image.url)
        return obj.intro_image.url

    class Meta:
        model = Settings
        fields = ["intro_image", "intro_header", "intro_text"]
