from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')
