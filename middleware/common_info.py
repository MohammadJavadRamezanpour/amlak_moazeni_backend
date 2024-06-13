from django.utils.deprecation import MiddlewareMixin

from settings.serializers import MenuesSerializer, SettingsSerializer
from settings.models import Settings, Menues


class CommonInfoMiddleware(MiddlewareMixin):
    def process_template_response(self, request, response):
        base = {
            "settings": SettingsSerializer(Settings.objects.all().last()).data,
            "menues": MenuesSerializer(
                Menues.objects.filter(parent__isnull=True, active=True), many=True
            ).data,
        }
        if hasattr(response, "data"):
            response.data["base"] = base
        return response
