from django.db import models


class User(models.Model):

    pkUser = models.AutoField(primary_key=True)
    username = models.TextField(null=False, blank=False, max_length=25)
    userpass = models.TextField(null=False, blank=False, max_length=25)
    alias = models.TextField(null=False, blank=False, max_length=25)
    karma = models.IntegerField(default=0, null=True)
    steamName = models.TextField(null=True)
    bnetName = models.TextField(null=True)
    horarioManana = models.BooleanField(default=False)
    horarioTarde = models.BooleanField(default=False)
    horarioNoche = models.BooleanField(default=False)
    horarioMadrugada = models.BooleanField(default=False)
    playOverwatch = models.BooleanField(default=False)
    playWow = models.BooleanField(default=False)
    playRust = models.BooleanField(default=False)
    playArk = models.BooleanField(default=False)
    playGta = models.BooleanField(default=False)
    playPubg = models.BooleanField(default=False)
    playFortnite = models.BooleanField(default=False)

