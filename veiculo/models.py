from django.db import models
from django.core.validators import RegexValidator
from empresas.models import Fabricante
from usuarios.models import Cliente


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
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fabricante = models.ForeignKey(Fabricante, related_name='veiculo', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.modelo} - {self.ano}'

    class Meta:
        db_table = 'veiculo'
