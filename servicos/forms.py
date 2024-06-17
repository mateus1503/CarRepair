from django import forms
from .models import Servico, OrdemServico


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'


class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        exclude = ['valorTotal']
