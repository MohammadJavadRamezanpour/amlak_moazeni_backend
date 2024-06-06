from rest_framework import serializers

from .base import BaseSerializer

class HomeSerializer(serializers.Serializer):
    base = BaseSerializer()
    

