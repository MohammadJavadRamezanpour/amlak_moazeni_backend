from django.utils.deprecation import MiddlewareMixin

from settings.serializers import MenuesSerializer, BaseSettingsSerializer
from settings.models import Settings, Menues




class CommonInfoMiddleware(MiddlewareMixin):
    def process_template_response(self, request, response):
        base = {
            "settings": BaseSettingsSerializer(Settings.objects.all().last()).data,
            "menues": MenuesSerializer(
                Menues.objects.filter(parent__isnull=True, active=True), many=True
            ).data,
        }
        if hasattr(response, "data"):
            from rest_framework.utils.serializer_helpers import ReturnList
            if type(response.data) == ReturnList:
                response.data = {
                    "result": response.data,
                    "base": base
                }
            else:
                response.data["base"] = base
        return response