from django.shortcuts import render
from .forms import ServicoForm
from .models import Servico
from django.http import HttpResponseRedirect
from django.urls import reverse


def add_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('add_servico'))
    else:
        form = ServicoForm()

    context = {'form': form}
    return render(request, 'servicos/add_servicos.html', context)


def list_servicos(request):
    servicos = Servico.objects.order_by('id')
    context = {'servicos': servicos}
    return render(request, 'servicos/list_servicos.html', context)

