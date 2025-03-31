from django.db import models
from django.db.models import CASCADE

class Category(models.Model):
    title  = models.CharField(max_length=16)

    def __str__(self):
        return  self.title

class Product(models.Model):
    product_name = models.CharField(max_length=16)
    description  =models.TextField()
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    have = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name
class Comment(models.Model):
    name = models.CharField(max_length=16)
    text = models.TextField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created_date =  models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name } - {self.product}'

