import graphene
from graphene_schema.types import CategoryType
from sales import models


class Query(object):
    all_categories = graphene.List(CategoryType)
    filter_category = graphene.List(
        CategoryType, category_id=graphene.Int(), category_title=graphene.String())

    def resolve_all_categories(self, info, **kwargs):
        return models.Category.objects.filter(state=True)

    def resolve_filter_category(self, info, **kwargs):
        category_id = kwargs.get('category_id')
        category_title = kwargs.get('category_title')
        if category_id is not None:
            return models.Category.objects.filter(id=category_id)
        if category_title is not None:
            return models.Category.objects.filter(title__icontains=category_title)
        return None
