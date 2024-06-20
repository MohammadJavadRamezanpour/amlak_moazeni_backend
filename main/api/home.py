from rest_framework.decorators import api_view
from rest_framework.response import Response

from settings.serializers import SliderSerializer, IntroSerializer
from settings.models import Slider, Settings
from store.models import Product, Category
from store.serializers import ProductSerializer, CategorySerializer

@api_view(['GET'])
def home_view(request):
    slider_queryset = Slider.objects.all().last()
    settings_queryset = Settings.objects.all().last()
    categories_queryset = Category.objects.all()

    serialized_slider = SliderSerializer(slider_queryset).data
    serialized_settings = IntroSerializer(settings_queryset).data
    serialized_categories = CategorySerializer(categories_queryset, many=True).data

    response = {
        "header": serialized_slider,
        "intro": serialized_settings,
        "categories": serialized_categories
    }

    return Response(response)
