import graphene
from graphene_schema.types import ProductType
from sales import models


class Query(object):
    all_products = graphene.List(ProductType)
    detail_product = graphene.Field(ProductType, product_id=graphene.Int())

    def resolve_all_products(self, info, **kwargs):
        return models.Product.objects.select_related('category').all()

    def resolve_detail_product(self, info, **kwargs):
        product_id = kwargs.get('product_id')
        if product_id is None:
            return None
        return models.Product.objects.filter(id=product_id).select_related('category')
