from django.db import models
from django.db.models import CASCADE

class Category(models.Model):
    title  = models.CharField(max_length=16)
class Product(models.Model):
    product_name = models.CharField(max_length=16)
    description  =models.TextField()
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
class Comment(models.Model):
    name = models.CharField(max_length=16)
