from django.db import models

class Mensaje(models.Model):

    pkMensaje = models.AutoField(primary_key=True)
    fkRemitente = models.IntegerField(null=False, blank=False)
    fkDestinatario = models.IntegerField(null=False, blank=False)
    asunto = models.TextField(max_length=150)
    cuerpo = models.TextField(max_length=1000)
    fecha = models.DateTimeField()

