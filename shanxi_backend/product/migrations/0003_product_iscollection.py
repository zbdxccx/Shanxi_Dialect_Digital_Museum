# Generated by Django 4.1.2 on 2022-11-28 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_product_image_url_product_introduction_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="isCollection",
            field=models.BooleanField(default=False),
        ),
    ]