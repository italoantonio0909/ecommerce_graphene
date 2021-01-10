import graphene
from graphene_schema.types import CategoryType
from sales import models


class CategoryCreate(graphene.Mutation):
    class Input:
        title = graphene.String()
    category = graphene.Field(CategoryType)

    @staticmethod
    def mutate(root, info, **kwargs):
        title = kwargs.get('title').strip()
        category = models.Category(title=title)
        category.save()
        return CategoryCreate(category=category)


class Mutation(graphene.AbstractType):
    category_create = CategoryCreate.Field()
