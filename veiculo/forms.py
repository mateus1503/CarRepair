from django import forms
from django.forms import PasswordInput
from .models import Veiculo


class VeiculoForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput())

    class Meta:
        model = Veiculo
        fields = '__all__'
