from django.forms import ModelForm
from .models import Cliente, Endereco


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        exclude = ("endereco",)


class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__"
