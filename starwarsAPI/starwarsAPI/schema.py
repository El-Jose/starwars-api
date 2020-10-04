import graphene
import starwars.schema


class Query(starwars.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)