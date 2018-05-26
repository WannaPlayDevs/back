import graphene
from graphene_django import DjangoObjectType

import datetime

from .models import Mensaje
from usuarios.schema import UserType
from usuarios.models import User

class MensajeType(DjangoObjectType):
    class Meta:
        model = Mensaje


class Query(graphene.ObjectType):
    mensajes = graphene.List(MensajeType)

    def resolve_mensajes(self, info, **kwargs):
        return Mensaje.objects.all()


class CreateMensaje(graphene.Mutation):
    pkMensaje = graphene.Int()
    fkRemitente = graphene.Field(UserType)
    fkDestinatario = graphene.Field(UserType)
    asunto = graphene.String()
    cuerpo = graphene.String()
    fecha = graphene.types.datetime.Date()

    class Arguments:
        fkRemitente = graphene.Int()
        fkDestinatario = graphene.Int()
        asunto = graphene.String()
        cuerpo = graphene.String()

    def mutate(self, info, fkRemitente, fkDestinatario, asunto, cuerpo):
        remitente = User.objects.filter(pkUser=fkRemitente).first()
        destinatario = User.objects.filter(pkUser=fkDestinatario).first()
        fecha = datetime.date.today()

        mensaje = Mensaje(
            fkRemitente=remitente, 
            fkDestinatario=destinatario, 
            asunto=asunto, 
            cuerpo=cuerpo, 
            fecha=fecha
        )
        mensaje.save()

        return CreateMensaje(
            pkMensaje=mensaje.pkMensaje,
            fkRemitente=mensaje.fkRemitente,
            fkDestinatario=mensaje.fkDestinatario,
            asunto=mensaje.asunto,
            cuerpo=mensaje.cuerpo,
            fecha=mensaje.fecha,
        )


class DeleteMensaje(graphene.ClientIDMutation):
    # permission_classes = (SomePermissionClass,)
    id = graphene.String()
    
    class Input:
        id = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        Mensaje.objects.get(pk=pkMensaje(input.get('paco'))[1]).delete()
        return DeleteMensaje()


class Mutation(graphene.ObjectType):
    create_mensaje = CreateMensaje.Field()
    delete_mensaje = DeleteMensaje.Field()

