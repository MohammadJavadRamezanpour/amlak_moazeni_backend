from rest_framework.decorators import api_view
from rest_framework.response import Response

from settings.serializers import SliderSerializer, IntroSerializer
from settings.models import Slider, Settings
from store.models import Category
from store.serializers import CategorySerializer
from blog.models import Post
from blog.serializers import PostListSerializer

@api_view(['GET'])
def home_view(request):
    slider_queryset = Slider.objects.all().last()
    settings_queryset = Settings.objects.all().last()
    categories_queryset = Category.objects.all()
    posts_queryset = Post.objects.filter(publish=True).order_by('-id')[:6]

    context = {"request": request}

    serialized_slider = SliderSerializer(slider_queryset, context=context).data
    serialized_settings = IntroSerializer(settings_queryset, context=context).data
    serialized_categories = CategorySerializer(categories_queryset, many=True, context=context).data
    serialized_posts = PostListSerializer(posts_queryset, many=True, context=context).data

    response = {
        "header": serialized_slider,
        "intro": serialized_settings,
        "categories": serialized_categories,
        "posts": serialized_posts,
    }

    return Response(response)
