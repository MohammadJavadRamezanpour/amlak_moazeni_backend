from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.serializers import base

@api_view(['GET'])
def home_view(request):
    return Response({})
