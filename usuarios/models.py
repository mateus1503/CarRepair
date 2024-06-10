from django.db import models
from core.models import Pessoa
from empresas.models import Empresa
from veiculo.models import Veiculo


class Funcionario(models.Model):
    password = models.CharField(max_length=20)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        db_table = 'funcionario'


class Cliente(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'cliente'
