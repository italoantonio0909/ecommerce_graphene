from sales import models
from graphene_schema.types import ProductType
import graphene


class ProductCreate(graphene.Mutation):
    class Input:
        title = graphene.String()
        description = graphene.String()
        price = graphene.Float()
        price_discount = graphene.Float()
        category = graphene.Int()
    product = graphene.Field(ProductType)

    def mutate(self, info, **kwargs):
        title = kwargs.get('title')
        description = kwargs.get('description')
        price = kwargs.get('price')
        price_discount = kwargs.get('price_discount')
        category = kwargs.get('category')
        product = models.Product.objects.create(
            title=title, description=description,
            price=price, price_discount=price_discount,
            category_id=category)
        return ProductCreate(product=product)


class Mutation(graphene.AbstractType):
    product_create = ProductCreate.Field()
