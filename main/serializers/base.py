from rest_framework import serializers

from settings.serializers import MenuesSerializer, SettingsSerializer
from settings.models import Settings, Menues

def get_base_info():
    return {
        "settings": SettingsSerializer(Settings.objects.all().last()).data,
        "menues": MenuesSerializer(Menues.objects.filter(parent__isnull=True, active=True), many=True).data
    }