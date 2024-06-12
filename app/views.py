from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
from .forms import ClienteForm


def horario_atual(request):
    horario_atual = datetime.datetime.now()
    return render(request, 'lista_horario.html', context={'horario_atual': horario_atual})


def exibir_template(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('horario_atual')

    form = ClienteForm
    return render(request, 'form_cliente.html', context={'form': form})
