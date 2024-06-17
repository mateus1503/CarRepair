from django import forms
from .models import *


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        exclude = ['telefone', 'endereco']
        labels = {'cpf': 'CPF'}
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'nome'}),
        }


class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = ['codigoArea', 'celular']
        labels = {'codigoArea': 'Código da Área'}
        widgets = {
            'codigoArea': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'logradouro', 'bairro', 'numero', 'complemento', 'cidade', 'estado']
        labels = {'cep': 'CEP'}

