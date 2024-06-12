from django import forms
from django.forms import PasswordInput
from .models import Funcionario, Cliente


class FuncionarioForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = Funcionario
        fields = ['password', 'pessoa', 'empresa']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
