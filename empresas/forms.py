from django import forms
from .models import Fabricante


class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = '__all__'
