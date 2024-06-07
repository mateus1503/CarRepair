from django.db import models
from core.models import Telefone


class Empresa(models.Model):
    razaoSocial = models.CharField(max_length=150)
    nomeFantasia = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18)
    email = models.EmailField()
    isMatriz = models.BooleanField(default=False)
    telefone = models.OneToOneField(Telefone, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'empresa'


class Fabricante(models.Model):
    razaoSocial = models.CharField(max_length=150)
    nomeSocial = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18)
    email = models.EmailField()
    telefone = models.OneToOneField(Telefone, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'fabricante'
