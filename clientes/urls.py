from django.urls import path
from .views import clientes_views
from .views.dependente_views import DependenteCreateView, DependenteListView
from .views.atendentes_views import (
    AtendenteCreateView,
    AtendenteListView,
)
from .views.usuario_views import (
     UsuarioCreateView, 
     UsuarioListView,
     UsuarioDetailView,
     UsuarioUpdateView,
     UsuarioDeleteView
)

urlpatterns = [
    path("clientes", clientes_views.clientes),
    path(
        "clientes_form",
        clientes_views.ClienteCreateView.as_view(),
        name="clientes_form",
    ),
    path(
        "clientes_list", clientes_views.ClienteListView.as_view(), name="clientes_list"
    ),
    path(
        "clientes_update/<int:pk>",
        clientes_views.ClienteUpdateView.as_view(),
        name="clientes_update",
    ),
    path(
        "lista_detail_clientes/<int:pk>",
        clientes_views.ClienteDetailView.as_view(),
        name="lista_detail_clientes",
    ),
    path(
        "delete_clientes/<int:pk>",
        clientes_views.ClienteDeleteView.as_view(),
        name="delete_clientes",
    ),
    path("form_dependente", DependenteCreateView.as_view(), name="form_dependente"),
    path("lista_dependentes", DependenteListView.as_view(), name="lista_dependentes"),
    path("form_atendente", AtendenteCreateView.as_view(), name="cadastrar_atendente"),
    path("lista_atendentes", AtendenteListView.as_view(), name="lista_atendentes"),
    path("form_usuario", UsuarioCreateView.as_view(), name="cadastrar_usuario"),
    path("lista_usuarios", UsuarioListView.as_view(), name="lista_usuarios"),
    path("lista_usuario/<int:pk>", UsuarioDetailView.as_view(), name="lista_usuario"),
    path("form_usuario/<int:pk>", UsuarioUpdateView.as_view(), name="editar_usuario"),
    path("remover_usuario/<int:pk>", UsuarioDeleteView.as_view(), name="remover_usuario"),
]
