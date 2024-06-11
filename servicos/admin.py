from django.contrib import admin
from .models import Servico, OrdemServico
from .forms import OrdemServicoForm


class OrdemServicoAdmin(admin.ModelAdmin):
    form = OrdemServicoForm


admin.site.register(Servico)
admin.site.register(OrdemServico)
