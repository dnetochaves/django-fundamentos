from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.views.generic import CreateView
from .models import Cliente

# Create your views here.
def clientes(request):
    horario_atual = datetime.datetime.now()
    return render(
        request,
        "clientes.html",
        context={"horario_atual": horario_atual},
    )


class ClienteCreateView(CreateView):
    model = Cliente
    fields = "__all__"
    template_name = "forms_clientes.html"