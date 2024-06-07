from django.db import models
from django.core.validators import RegexValidator


TIPOS_VEICULOS = [
    (1, 'Carro'),
    (2, 'Caminhão'),
    (3, 'Picape'),
]


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
    tipo = models.IntegerField(choices=TIPOS_VEICULOS)

    class Meta:
        db_table = 'veiculo'
