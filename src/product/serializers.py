from rest_framework import serializers
from product.models import Product, Category


# only if you want to create categories with api. now - you can do it in Admin part.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = "__all__"
