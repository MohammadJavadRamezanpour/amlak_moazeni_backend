from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.api import PostViewSet, CategoryViewSet

router = DefaultRouter()
router.register('post', PostViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]