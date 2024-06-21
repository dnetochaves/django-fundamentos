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
from .models import Cliente, Endereco
from django.urls import reverse_lazy, reverse
from .forms import ClienteForm, EnderecoForm


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
    form_class = ClienteForm
    template_name = "forms_clientes.html"
    success_url = "clientes_list"

    def get_context_data(self, **kwargs):
        context = super(ClienteCreateView, self).get_context_data(**kwargs)
        context["form"] = ClienteForm
        context["endereco_form"] = EnderecoForm
        return context

    def post(self, request, *args, **kwargs):
        cliente_form = ClienteForm(data=request.POST)
        endereco_form = EnderecoForm(data=request.POST)
        if cliente_form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.endereco = endereco
            cliente.save()
            return HttpResponseRedirect(reverse("clientes_list"))


class ClienteListView(ListView):
    model = Cliente
    template_name = "lista_clientes.html"


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "forms_clientes.html"
    success_url = reverse_lazy("clientes_list")  # "/clientes/clientes_list"

    def get_context_data(self, **kwargs):
        context = super(ClienteUpdateView, self).get_context_data(**kwargs)
        context["form"] = ClienteForm(instance=self.object)
        context["endereco_form"] = EnderecoForm(instance=self.object.endereco)
        return context
    
    def post(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(id=kwargs["pk"])
        cliente_form = ClienteForm(data=request.POST or None, instance=cliente)
        endereco_form = EnderecoForm(data=request.POST or None, instance=cliente.endereco)
        if cliente_form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.endereco = endereco
            cliente.save()
            return HttpResponseRedirect(reverse("clientes_list"))

    


class ClienteDetailView(DetailView):
    model = Cliente
    fields = "__all__"
    template_name = "lista_detail_clientes.html"
    context_object_name = "cliente"


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes_list")  # "/clientes/clientes_list"

    def post(self, request, *args, **kwargs):
        cliente = Cliente.objects.get(id=kwargs["pk"])
        print(cliente.pk)
        cliente.endereco.delete()
        cliente.delete()
        return HttpResponseRedirect(reverse("clientes_list"))
