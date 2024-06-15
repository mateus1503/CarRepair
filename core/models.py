from django.db import models


SEXO = {
    (1, 'Masculino'),
    (2, 'Feminino'),
}


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    sexo = models.IntegerField(choices=SEXO)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        db_table = 'pessoa'


class Telefone(models.Model):
    codigoArea = models.CharField(max_length=3)
    celular = models.CharField(max_length=9, unique=True)
    pessoa = models.ForeignKey(Pessoa, related_name='telefone', on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.codigoArea}) {self.celular}'

    class Meta:
        db_table = 'telefone'


class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.PositiveIntegerField()
    complemento = models.CharField(max_length=150, null=False, blank=True)
    bairro = models.CharField(max_length=150)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=100)
    pessoa = models.ForeignKey(Pessoa, related_name='endereco', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.bairro}, {self.logradouro}, {self.numero}'

    class Meta:
        db_table = 'endereco'
