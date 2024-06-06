from rest_framework import serializers

from settings.models import Menues

class MenuesSerializer(serializers.ModelSerializer):
    sub_menues = serializers.SerializerMethodField()

    def get_sub_menues(self, instance):
        return MenuesSerializer(instance.sub_menues).data
    
    class Meta:
        model = Menues
        fields = ["icon", "text", "link", "sub_menues"]
