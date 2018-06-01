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


class UpdateUser(graphene.Mutation):
    pkUser = graphene.Int()
    username = graphene.String()
    password = graphene.String()
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
        pkUser = graphene.Int()
        username = graphene.String()
        password = graphene.String()
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

    def mutate(self, info, pkUser, username=None, password=None, alias=None,
               karma=None, steamName=None, bnetName=None, horarioManana=None,
               horarioTarde=None, horarioNoche=None, horarioMadrugada=None,
               playOverwatch=None, playWow=None, playRust=None, playArk=None,
               playGta=None, playPubg=None, playFortnite=None):
        user = User.objects.get(pkUser=pkUser)

        if (username is not None):
            user.username = username
            user.save()
        if (password is not None):
            user.password = password
            user.save()
        if (alias is not None):
            user.alias = alias
            user.save()
        if (karma is not None):
            user.karma = karma
            user.save()
        if (steamName is not None):
            user.steamName = steamName
            user.save()
        if (bnetName is not None):
            user.bnetName = bnetName
            user.save()
        if (horarioManana is not None):
            user.horarioManana = horarioManana
            user.save()
        if (horarioTarde is not None):
            user.horarioTarde = horarioTarde
            user.save()
        if (horarioNoche is not None):
            user.horarioNoche = horarioNoche
            user.save()
        if (horarioMadrugada is not None):
            user.horarioMadrugada = horarioMadrugada
            user.save()
        if (playOverwatch is not None):
            user.playOverwatch = playOverwatch
            user.save()
        if (playWow is not None):
            user.playWow = playWow
            user.save()
        if (playRust is not None):
            user.playRust = playRust
            user.save()
        if (playArk is not None):
            user.playArk = playArk
            user.save()
        if (playGta is not None):
            user.playGta = playGta
            user.save()
        if (playPubg is not None):
            user.playPubg = playPubg
            user.save()
        if (playFortnite is not None):
            user.playFortnite = playFortnite
            user.save()

        return user



class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
