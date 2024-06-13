from django.shortcuts import render
from django.urls import reverse
from .forms import ClienteForm
from core.forms import PessoaForm, TelefoneForm, EnderecoForm
from django.http import HttpResponseRedirect


def add_cliente(request):
    if request.method == 'POST':
        formCliente = ClienteForm(request.POST)
        formPessoa = PessoaForm(request.POST)
        formEndereco = EnderecoForm(request.POST)
        formTelefone = TelefoneForm(request.POST)
        if formCliente.is_valid() and formPessoa.is_valid() and formEndereco.is_valid() and formTelefone.is_valid():
            endereco = formEndereco.save()
            telefone = formTelefone.save()
            pessoa = formPessoa.save(commit=False)
            pessoa.endereco = endereco
            pessoa.telefone = telefone
            pessoa.save()
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
