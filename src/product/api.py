from io import BytesIO
from tempfile import NamedTemporaryFile

import requests
from django.core.files import File
from django_filters import rest_framework as filters
from PIL import Image
from rest_framework import permissions, viewsets

from product.models import Product
from product.permissions import RoleIsAdmin, RoleIsManager
from product.serializers import ProductRequestSerializer, ProductResponseSerializer


class ProductFilter(filters.FilterSet):
    offer_of_the_month = filters.BooleanFilter()
    available = filters.BooleanFilter()
    pickup = filters.BooleanFilter()

    class Meta:
        model = Product
        fields = ["offer_of_the_month", "available", "pickup"]


class ProductViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Product.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return ProductRequestSerializer
        return ProductResponseSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "list":
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ["create", "update", "partial_update"]:
            permission_classes = [RoleIsAdmin | RoleIsManager]
        elif self.action == "destroy":
            permission_classes = [RoleIsAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]

    def _process_photo_from_url(self, product, photo_url):
        # Download the image from the URL using requests library
        response = requests.get(photo_url, headers={"User-Agent": "Mozilla/5.0"})
        image_temp = NamedTemporaryFile(delete=True)
        image_temp.write(response.content)
        image_temp.flush()

        # Process the image
        im = Image.open(image_temp)
        size = (800, 800)
        im.thumbnail(size, Image.ANTIALIAS)

        thumb_io = BytesIO()
        im.save(thumb_io, format="JPEG")
        im.close()

        # Assign to the photo field
        product.photo.save(f"product_{product.id}.jpg", File(thumb_io))

    def perform_create(self, serializer):
        photo_url = serializer.validated_data.pop("photo", None)
        product = serializer.save()
        if photo_url:
            self._process_photo_from_url(product, photo_url)

    def perform_update(self, serializer):
        photo_url = serializer.validated_data.pop("photo", None)
        product = serializer.save()
        if photo_url:
            self._process_photo_from_url(product, photo_url)
