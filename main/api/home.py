from rest_framework.generics import RetrieveAPIView

from main.serializers import HomeSerializer

class HomeView(RetrieveAPIView):
    serializer_class = HomeSerializer
