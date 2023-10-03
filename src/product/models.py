from io import BytesIO

from django.core.exceptions import ValidationError
from django.core.files import File
from django.core.validators import FileExtensionValidator
from django.db import models
from PIL import Image


class Product(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to="product_photos/",
        validators=[FileExtensionValidator(["jpg", "jpeg", "png"])],
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
                self._process_photo()
        elif self.photo:
            self._process_photo()

        super().save(*args, **kwargs)

    def _process_photo(self):
        try:
            im = Image.open(self.photo)
            size = (800, 800)
            im.thumbnail(size, Image.ANTIALIAS)

            thumb_io = BytesIO()
            im.save(thumb_io, format="JPEG")
            im.close()

            file_name = self.photo.name
            self.photo = File(thumb_io, name=file_name)

        except Exception as e:
            raise ValidationError(f"Error processing image: {e}")

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
