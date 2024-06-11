from django.contrib.auth.hashers import make_password
from django.db import models
from core.models import Pessoa
from empresas.models import Empresa
from veiculo.models import Veiculo


class Funcionario(models.Model):
    password = models.CharField(max_length=255)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Funcionario, self).save(*args, **kwargs)

    def __str__(self):
        return self.pessoa.nome

    class Meta:
        db_table = 'funcionario'


class Cliente(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.pessoa.nome

    class Meta:
        db_table = 'cliente'
