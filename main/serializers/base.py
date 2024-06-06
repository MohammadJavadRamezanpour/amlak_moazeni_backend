from rest_framework import serializers

from settings.serializers import MenuesSerializer, SettingsSerializer
from settings.models import Settings, Menues

class BaseSerializer(serializers.Serializer):
    base = serializers.SerializerMethodField()

    def get_base(self):
        settings = SettingsSerializer(Settings.objects.all().last()).data
        menues = MenuesSerializer(MenuesSerializer.objects.filter(parent__isnull=True, active=True)).data
        return dict(settings=settings, menues=menues)