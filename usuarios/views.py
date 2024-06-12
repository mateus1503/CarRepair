from django.shortcuts import render
from django.urls import reverse
from .forms import ClienteForm
from core.forms import PessoaForm, TelefoneForm, EnderecoForm
from django.http import HttpResponseRedirect


def add_cliente(request):
    if request.method == 'POST':
        formCliente = ClienteForm(request.POST)
        formPessoa = PessoaForm(request.POST)
        formTelefone = TelefoneForm(request.POST)
        formEndereco = EnderecoForm(request.POST)
        if formCliente.is_valid() and formPessoa.is_valid() and formTelefone.is_valid and formEndereco.is_valid():
            telefone = formTelefone.save()
            endereco = formEndereco.save()
            pessoa = formPessoa.save(commit=False)
            pessoa.telefone = telefone
            pessoa.endereco = endereco
            pessoa = pessoa.save()
            cliente = formCliente.save(commit=False)
            cliente.pessoa = pessoa
            cliente.save()
            return HttpResponseRedirect(reverse('add_cidade'))
    else:
        formCliente = ClienteForm()
        formPessoa = PessoaForm()
        formTelefone = TelefoneForm()
        formEndereco = EnderecoForm()

    context = dict(formCliente=formCliente, formPessoa=formPessoa, formTelefone=formTelefone, formEndereco=formEndereco)
    return render(request, 'usuarios/add_cliente.html', context)
