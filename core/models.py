from django.db import models


SEXO = {
    (1, 'Masculino'),
    (2, 'Feminino'),
}


class Estado(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = 'estado'


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, related_name='cidade', on_delete=models.CASCADE)

    class Meta:
        db_table = 'cidade'


class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.PositiveIntegerField()
    complemento = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cep = models.CharField(max_length=8)
    cidade = models.ForeignKey(Cidade, related_name='endereco', on_delete=models.CASCADE)

    class Meta:
        db_table = 'endereco'


class Telefone(models.Model):
    codigoArea = models.CharField(max_length=3)
    numero = models.CharField(max_length=9)

    class Meta:
        db_table = 'telefone'


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    sexo = models.IntegerField(choices=SEXO)
    telefone = models.ForeignKey(Telefone, related_name='pessoa', on_delete=models.SET_NULL, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, related_name='pessoa', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'pessoa'
