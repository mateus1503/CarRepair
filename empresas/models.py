from django.db import models
from core.models import Telefone, Endereco


class Empresa(models.Model):
    razaoSocial = models.CharField(max_length=150)
    nomeFantasia = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField()
    isMatriz = models.BooleanField(default=False)
    telefone = models.OneToOneField(Telefone, related_name='empresa', on_delete=models.SET_NULL, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, related_name='empresa', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nomeFantasia

    class Meta:
        db_table = 'empresa'


class Fabricante(models.Model):
    razaoSocial = models.CharField(max_length=150)
    nomeFantasia = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.OneToOneField(Telefone, related_name='fabricante', on_delete=models.SET_NULL, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, related_name='fabricante', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nomeFantasia

    class Meta:
        db_table = 'fabricante'
