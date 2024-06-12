from django.shortcuts import render
from django.http import HttpResponse
import datetime


def horario_atual(request):
    horario_atual = datetime.datetime.now()
    return HttpResponse(horario_atual)
