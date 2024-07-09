from django import forms
from .models import Veiculo


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'
        exclude = ['cliente']

    def __init__(self, *args, **kwargs):
        super(VeiculoForm, self).__init__(*args, **kwargs)
        self.fields['fabricante'].widget.attrs.update({
            'class': 'form-select',
            'id': 'inputGroupSelect04',
        }),
        self.fields['tipo'].widget.attrs.update({
            'class': 'form-select',
            'id': 'inputGroupSelect04',
        }),
