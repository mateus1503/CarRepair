from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from empresas.models import Empresa
from usuarios.models import Funcionario, Cliente

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

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'servico'


class OrdemServico(models.Model):
    observacao = models.TextField(max_length=255)
    dataInicial = models.DateTimeField(auto_now_add=True)
    dataFinal = models.DateTimeField()
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
    servico = models.ManyToManyField(Servico, related_name='ordemServico')
    cliente = models.ForeignKey(Cliente, related_name='ordemServico', on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, related_name='ordemServico', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(choices=STATUS)

    class Meta:
        db_table = 'ordemServico'

    def total_servico(self):
        total = 0
        for servico in self.servico.all():
            total += servico.valor

        self.valorTotal = total
        self.save()
