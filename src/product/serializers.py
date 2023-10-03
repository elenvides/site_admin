from rest_framework import serializers

from product.models import Category, Product


# only if you want to create categories with api. now - you can do it in Admin part.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductRequestSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    photo = serializers.CharField(required=False)

    class Meta:
        model = Product
        fields = "__all__"


class ProductResponseSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    photo_url = serializers.ImageField(source="photo", use_url=True)

    class Meta:
        model = Product
        fields = "__all__"
