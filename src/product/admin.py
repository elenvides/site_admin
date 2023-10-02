from django.contrib import admin

from product.models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "category",
        "price",
        "offer_of_the_month",
        "available",
        "pickup",
    ]
    list_filter = ["category", "offer_of_the_month", "available", "pickup"]
    search_fields = ["id", "name", "short_description", "long_description"]
    readonly_fields = ["id"]
    ordering = ["id"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "photo",
                    "category",
                    "price",
                    "offer_of_the_month",
                    "available",
                    "pickup",
                )
            },
        ),
        ("Description", {"fields": ("short_description", "long_description")}),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["id", "name"]
    readonly_fields = ["id"]
    ordering = ["id"]
