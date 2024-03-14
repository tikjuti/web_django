from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200, default="")
    slug = models.CharField(max_length=200, default="")
    description = models.TextField(default="")
    active = models.BooleanField(default=True)
    
class Product(models.Model):
    title = models.CharField(max_length=200, default="")
    image = models.ImageField()
    description = models.TextField(default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    active = models.BooleanField(default=True)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="")
    price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    inventory = models.IntegerField(default=0)
    active = models.BooleanField(default=True)