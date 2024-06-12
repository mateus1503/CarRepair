from django import forms
from .models import *


class CidadeForm(forms.ModelForm):
    estado = forms.ModelChoiceField(queryset=Estado.objects.order_by('nome'))

    class Meta:
        model = Cidade
        fields = ['nome', 'estado']


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        exclude = ['telefone', 'endereco']


class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = '__all__'


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'
