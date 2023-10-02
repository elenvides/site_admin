from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions
from product.models import Product
from product.serializers import ProductSerializer
from product.permissions import RoleIsAdmin, RoleIsManager


class ProductFilter(filters.FilterSet):
    offer_of_the_month = filters.BooleanFilter()
    available = filters.BooleanFilter()
    pickup = filters.BooleanFilter()

    class Meta:
        model = Product
        fields = ['offer_of_the_month', 'available', 'pickup']


class ProductViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [RoleIsAdmin | RoleIsManager]
        elif self.action == 'destroy':
            permission_classes = [RoleIsAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]
