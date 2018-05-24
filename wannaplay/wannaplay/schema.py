import graphene

import users.schema
import amigos.schema
import mensajes.schema


class Query(users.schema.Query, amigos.schema.Query, mensajes.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, amigos.schema.Mutation, mensajes.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
