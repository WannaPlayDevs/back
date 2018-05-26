import graphene
from graphene_django import DjangoObjectType

from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()


class CreateUser(graphene.Mutation):
    pkUser = graphene.Int()
    username = graphene.String()
    userpass = graphene.String()
    alias = graphene.String()
    karma = graphene.Int()
    steamName = graphene.String()
    bnetName = graphene.String()
    horarioManana = graphene.Boolean()
    horarioTarde = graphene.Boolean()
    horarioNoche = graphene.Boolean()
    horarioMadrugada = graphene.Boolean()
    playOverwatch = graphene.Boolean()
    playWow = graphene.Boolean()
    playRust = graphene.Boolean()
    playArk = graphene.Boolean()
    playGta = graphene.Boolean()
    playPubg = graphene.Boolean()
    playFortnite = graphene.Boolean()

    class Arguments:
        username = graphene.String()
        userpass = graphene.String()
        alias = graphene.String()
        karma = graphene.Int()
        steamName = graphene.String()
        bnetName = graphene.String()
        horarioManana = graphene.Boolean()
        horarioTarde = graphene.Boolean()
        horarioNoche = graphene.Boolean()
        horarioMadrugada = graphene.Boolean()
        playOverwatch = graphene.Boolean()
        playWow = graphene.Boolean()
        playRust = graphene.Boolean()
        playArk = graphene.Boolean()
        playGta = graphene.Boolean()
        playPubg = graphene.Boolean()
        playFortnite = graphene.Boolean()

    def mutate(self, info, username, userpass, alias, karma, steamName, bnetName, horarioManana, horarioTarde, horarioNoche, horarioMadrugada,
               playOverwatch, playWow, playRust, playArk, playGta, playPubg, playFortnite):
        user = User(username=username, userpass=userpass, alias=alias, karma=karma, steamName=steamName, bnetName=bnetName,
                    horarioManana=horarioManana, horarioTarde=horarioTarde, horarioNoche=horarioNoche, horarioMadrugada=horarioMadrugada,
                    playOverwatch=playOverwatch, playWow=playWow, playRust=playRust, playArk=playArk, playGta=playGta, playPubg=playPubg, playFortnite=playFortnite)
        user.save()

        return CreateUser(
            pkUser=pkUser,
            username=username,
            userpass=userpass,
            alias=alias,
            karma=karma,
            steamName=steamName,
            bnetName=bnetName,
            horarioManana=horarioManana,
            horarioTarde=horarioTarde,
            horarioNoche=horarioNoche,
            horarioMadrugada=horarioMadrugada,
            playOverwatch=playOverwatch,
            playWow=playWow,
            playRust=playRust,
            playArk=playArk,
            playGta=playGta,
            playPubg=playPubg,
            playFortnite=playFortnite
        )


class DeleteUser(graphene.ClientIDMutation):
    permission_classes = (SomePermissionClass,)

    class Input:
        id = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        User.objects.get(pk=pkUser(input.get('id'))[1]).delete()
        return DeleteUser()


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()

