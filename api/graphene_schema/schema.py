import graphene
from graphene_schema.query.category import Query as CategoryQuery
from graphene_schema.mutation.category import Mutation as CategoryMutation
from graphene_schema.query.product import Query as ProductQuery
from graphene_schema.mutation.product import Mutation as ProductMutation


class Query(CategoryQuery, ProductQuery, graphene.ObjectType):
    pass


class Mutation(CategoryMutation, ProductMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
