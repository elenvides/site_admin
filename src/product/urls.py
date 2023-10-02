from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.api import ProductViewSet

router = DefaultRouter()
router.register("", ProductViewSet, basename="products")

urlpatterns = [
    path('', include(router.urls)),
]
