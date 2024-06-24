from django.views.generic import CreateView, ListView


from clientes.forms.atentende_forms import AtendenteForm
from clientes.models import Atendente


class AtendenteCreateView(CreateView):
    model = Atendente
    form_class = AtendenteForm
    template_name = "atendentes/forms_atendentes.html"
    success_url = "lista_atendentes"


class AtendenteListView(ListView):
    print("aqui")
    model = Atendente
    template_name = "atendentes/lista_atendentes.html"
