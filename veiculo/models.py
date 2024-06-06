from django.db import models
from django.core.validators import RegexValidator


class Tipo(models.IntegerField):
    CARRO = 1, 'Carro'
    CAMINHAO = 2, 'Caminhao'
    PICAPE = 3, 'Picape'


class Veiculo(models.Model):
    modelo = models.CharField(max_length=255)
    ano = models.CharField(max_length=4)
    placa = models.CharField(
        max_length=8,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{3}[0-9]{4}$',
                message='A placa deve ter o formato AAA-9999.',
                code='invalid_placa'
            )
        ]
    )
    chassi = models.CharField(max_length=17)
    tipo = models.IntegerField(choices=Tipo.choices)


class Fabricante(models.Model):
    razaoSocial = models.CharField(max_length=255)
    nomeFantasia = models.CharField(max_length=255)
    email = models.EmailField()
    cnpj = models.CharField(max_length=18)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
