from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CidadeForm


def add_cidade(request):
    if request.method == 'POST':
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('add_cidade'))
    else:
        form = CidadeForm()

    context = {'form': form}
    return render(request, 'core/add_cidade.html', context)
