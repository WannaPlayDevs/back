from django.db import models

class Amigo(models.Model):

    pkAmigo = models.AutoField(primary_key=True)
    fkUser1 = models.models.ForeignKey(User, on_delete=models.CASCADE, related_name="pkUsuario")
    fkUser2 = models.models.ForeignKey(User, on_delete=models.CASCADE, related_name="pkUsuario")
    estado = models.IntegerField(null=False, blank=False)
    fecha = models.DateTimeField()

