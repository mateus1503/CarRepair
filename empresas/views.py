from django.shortcuts import render
from .forms import FabricanteForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def add_fabricantes(request):
    if request.method == 'POST':
        form = FabricanteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('add_veiculos'))
    else:
        form = FabricanteForm()

    context = {'form': form}
    return render(request, 'empresas/add_fabricante.html', context)
