from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from clientes.models import User
from django.contrib.auth.models import User 

class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UsuarioUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )