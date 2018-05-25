import graphene

import usuarios.schema
import amigos.schema
import mensajes.schema


class Query(usuarios.schema.Query, amigos.schema.Query, mensajes.schema.Query, graphene.ObjectType):
    pass


class Mutation(usuarios.schema.Mutation, amigos.schema.Mutation, mensajes.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
