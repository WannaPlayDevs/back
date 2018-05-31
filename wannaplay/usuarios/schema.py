import graphene
from graphene_django import DjangoObjectType

from django.db.models import Max

from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    me = graphene.Field(UserType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Invalid token!')

        return user


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String()
        password = graphene.String()
        alias = graphene.String()

    def mutate(self, info, username, password, alias):
        user = User(username=username, alias=alias)
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class DeleteUser(graphene.ClientIDMutation):
    # permission_classes = (SomePermissionClass,)

    class Input:
        id = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        User.objects.get(pk=pkUser(input.get('id'))[1]).delete()
        return DeleteUser()


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()

