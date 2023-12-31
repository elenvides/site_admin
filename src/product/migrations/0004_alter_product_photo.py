# Generated by Django 4.2.5 on 2023-10-03 11:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_alter_category_options_alter_product_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="photo",
            field=models.ImageField(
                upload_to="product_photos/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        ["jpg", "jpeg", "png"]
                    )
                ],
            ),
        ),
    ]
