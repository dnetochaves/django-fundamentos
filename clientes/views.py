from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .models import Cliente
from django.urls import reverse_lazy


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
    success_url = "clientes_list"


class ClienteListView(ListView):
    model = Cliente
    template_name = "lista_clientes.html"


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = "__all__"
    template_name = "forms_clientes.html"
    success_url = reverse_lazy("clientes_list")  # "/clientes/clientes_list"


class ClienteDetailView(DetailView):
    model = Cliente
    fields = "__all__"
    template_name = "lista_detail_clientes.html"
    context_object_name = "cliente"


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes_list")  # "/clientes/clientes_list"
