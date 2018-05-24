from django.db import models

class Mensaje(models.Model):

    pkMensaje = models.AutoField(primary_key=True)
    fkRemitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pkUsuario")
    fkDestinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pkUsuario")
    asunto = models.TextField(max_length=150)
    cuerpo = models.TextField(max_length=1000)
    fecha = models.DateTimeField()

