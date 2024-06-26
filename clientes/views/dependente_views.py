from django.views.generic import CreateView, ListView


from ..forms.dependentes_forms import DependenteForm
from ..models import Dependente


class DependenteCreateView(CreateView):
    model = Dependente
    form_class = DependenteForm
    template_name = "dependentes/form_dependente.html"
    success_url = "lista_atendentes"


class DependenteListView(ListView):
    model = Dependente
    template_name = "dependentes/lista_dependentes.html"
