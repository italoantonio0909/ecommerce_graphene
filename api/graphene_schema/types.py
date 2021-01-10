import graphene
from graphene_django.types import DjangoObjectType
from sales import models


class ProductType(DjangoObjectType):
    class Meta:
        model = models.Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = models.Category
