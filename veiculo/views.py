from django.shortcuts import render
from .forms import VeiculoForm
from usuarios.models import Cliente
from django.http import HttpResponseRedirect
from django.urls import reverse


def add_veiculos(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)

    if request.method == 'POST':
        form = VeiculoForm(data=request.POST)
        if form.is_valid():
            form.cliente = cliente
            form.save()
            return HttpResponseRedirect(reverse('add_veiculos', args=[cliente_id]))
    else:
        form = VeiculoForm()

    context = {'form': form, 'cliente': cliente}
    return render(request, 'veiculo/add_veiculos.html', context)
