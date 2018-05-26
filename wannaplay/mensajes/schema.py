import graphene
from graphene_django import DjangoObjectType

from .models import Mensaje


class MensajeType(DjangoObjectType):
    class Meta:
        model = Mensaje


class Query(graphene.ObjectType):
    mensajes = graphene.List(MensajeType)

    def resolve_mensajes(self, info, **kwargs):
        return Mensaje.objects.all()


class CreateMensaje(graphene.Mutation):
    pkMensaje = graphene.Int()
    fkRemitente = graphene.Int()
    fkDestinatario = graphene.Int()
    asunto = graphene.String()
    cuerpo = graphene.String()
    fecha = graphene.String()

    class Arguments:
        fkRemitente = graphene.Int()
        fkDestinatario = graphene.Int()
        asunto = graphene.String()
        cuerpo = graphene.String()
        fecha = graphene.String()

    def mutate(self, info, fkRemitente, fkDestinatario, asunto, cuerpo, fecha):
        mensaje = Mensaje(fkRemitente=fkRemitente, fkDestinatario=fkDestinatario, asunto=asunto, cuerpo=cuerpo, fecha=fecha)
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
    permission_classes = (SomePermissionClass,)

    class Input:
        id = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        Mensaje.objects.get(pk=pkMensaje(input.get('id'))[1]).delete()
        return DeleteMensaje()


class Mutation(graphene.ObjectType):
    create_mensaje = CreateMensaje.Field()
    delete_mensaje = DeleteMensaje.Field()

