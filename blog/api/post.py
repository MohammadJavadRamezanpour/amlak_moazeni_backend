from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Post
from ..serializers import PostSerializer, PostListSerializer
from ..filters import PostFilter
from core.misc import CustomPaginationClass

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(publish=True).order_by('-created_at')
    pagination_class = CustomPaginationClass      
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'tags__text']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    filterset_class = PostFilter

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer
        return PostSerializer
