from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, null=False)
    state = models.BooleanField(default=True)


class Product(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=False)
    price = models.FloatField()
    price_discount = models.FloatField()
    created_on = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    state = models.BooleanField(default=True)
