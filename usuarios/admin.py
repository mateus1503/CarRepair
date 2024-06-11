from django.contrib import admin
from .models import Funcionario, Cliente
from .forms import FuncionarioForm
from django.forms import PasswordInput


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    form = FuncionarioForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['password'].widget = PasswordInput(render_value=False)
        return form


admin.site.register(Cliente)
