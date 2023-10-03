from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to="product_photos/",
    )
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    offer_of_the_month = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    pickup = models.BooleanField(default=True)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # if object exists
        if self.pk:
            orig = Product.objects.get(pk=self.pk)
            # if photo was changed
            if orig.photo != self.photo:
                # delete old photo
                orig.photo.delete(save=False)

        super().save(*args, **kwargs)

    class Meta:
        db_table = "products"
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "categories"
        ordering = ["-id"]

    def __str__(self):
        return self.name
