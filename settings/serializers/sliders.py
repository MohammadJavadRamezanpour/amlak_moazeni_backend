from rest_framework import serializers

from settings.models import Slider

class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = ["image", "title", "text"]
        read_only_fields = ["image", "title", "text"]