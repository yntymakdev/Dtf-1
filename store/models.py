from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=16)
    description  =models.TextField()
    price = models.PositiveIntegerField(default=0)
