from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import datetime


def horario_atual(request):
    horario_atual = datetime.datetime.now()
    return render(request, 'lista_horario.html', context={'horario_atual': horario_atual})
