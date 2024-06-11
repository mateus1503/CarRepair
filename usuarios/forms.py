from django import forms
from django.forms import PasswordInput
from .models import Funcionario


class FuncionarioForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = Funcionario
        fields = ['password', 'pessoa', 'empresa']
