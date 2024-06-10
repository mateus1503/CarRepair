from django.db import models
from empresas.models import Empresa
from usuarios.models import Funcionario

STATUS = {
    (1, 'Aberto'),
    (2, 'Em Andamento'),
    (3, 'Finalizado'),
    (4, 'Cancelado'),
}


class Servico(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    empresa = models.ForeignKey(Empresa, related_name='servico', on_delete=models.CASCADE)

    class Meta:
        db_table = 'servico'


class OrdemServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models)

