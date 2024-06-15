from django import forms
from .models import *


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        exclude = ['telefone', 'endereco']
        labels = {'cpf': 'CPF'}


class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = ['codigoArea', 'celular']
        labels = {'codigoArea': 'Código da Área'}


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'logradouro', 'bairro', 'numero', 'complemento', 'cidade', 'estado']
        labels = {'cep': 'CEP'}
