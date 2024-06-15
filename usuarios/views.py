from django.shortcuts import render
from django.urls import reverse
from .forms import ClienteForm
from core.forms import PessoaForm, TelefoneForm, EnderecoForm
from django.http import HttpResponseRedirect

from .models import Cliente


def add_cliente(request):
    if request.method == 'POST':
        formCliente = ClienteForm(request.POST)
        formPessoa = PessoaForm(request.POST)
        formEndereco = EnderecoForm(request.POST)
        formTelefone = TelefoneForm(request.POST)
        if formCliente.is_valid() and formPessoa.is_valid() and formEndereco.is_valid() and formTelefone.is_valid():
            pessoa = formPessoa.save()
            telefone = formTelefone.save(commit=False)
            telefone.pessoa = pessoa
            telefone.save()
            endereco = formEndereco.save(commit=False)
            endereco.pessoa = pessoa
            endereco.save()
            cliente = formCliente.save(commit=False)
            cliente.pessoa = pessoa
            cliente.save()
            return HttpResponseRedirect(reverse('add_cliente'))
    else:
        formCliente = ClienteForm()
        formPessoa = PessoaForm()
        formEndereco = EnderecoForm()
        formTelefone = TelefoneForm()

    context = dict(formCliente=formCliente, formPessoa=formPessoa, formEndereco=formEndereco, formTelefone=formTelefone)
    return render(request, 'usuarios/add_cliente.html', context)


def list_clientes(request):
    clientes = Cliente.objects.order_by('id')

    context = {'clientes': clientes}
    return render(request, 'usuarios/list_clientes.html', context)
