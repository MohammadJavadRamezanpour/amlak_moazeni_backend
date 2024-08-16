from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.api import ProductViewset, CategoryViewSet

router = DefaultRouter()
router.register('product', ProductViewset)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]