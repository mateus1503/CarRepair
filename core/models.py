from django.db import models


SEXO = {
    (1, 'Masculino'),
    (2, 'Feminino'),
}


class Estado(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome} - {self.sigla}'

    class Meta:
        db_table = 'estado'


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, related_name='cidade', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}, {self.estado.sigla}'

    class Meta:
        db_table = 'cidade'


class Endereco(models.Model):
    logradouro = models.CharField(max_length=255)
    numero = models.PositiveIntegerField()
    complemento = models.CharField(max_length=150, null=False, blank=True)
    bairro = models.CharField(max_length=150)
    cep = models.CharField(max_length=8)
    cidade = models.ForeignKey(Cidade, related_name='endereco', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.bairro}, {self.logradouro}, {self.numero}'

    class Meta:
        db_table = 'endereco'


class Telefone(models.Model):
    codigoArea = models.CharField(max_length=3)
    celular = models.CharField(max_length=9, unique=True)

    def __str__(self):
        return f'({self.codigoArea}) {self.numero}'

    class Meta:
        db_table = 'telefone'


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    sexo = models.IntegerField(choices=SEXO)
    telefone = models.ForeignKey(Telefone, related_name='pessoa', on_delete=models.SET_NULL, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, related_name='pessoa', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        db_table = 'pessoa'
