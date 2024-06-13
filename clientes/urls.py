from django.urls import path
from . import views

urlpatterns = [
    path("clientes", views.clientes),
    path("clientes_form", views.ClienteCreateView.as_view(), name="clientes_form"),
    path("clientes_list", views.ClienteListView.as_view(), name="clientes_list"),
    path(
        "clientes_update/<int:pk>",
        views.ClienteUpdateView.as_view(),
        name="clientes_update",
    ),
    path(
        "lista_detail_clientes/<int:pk>",
        views.ClienteDetailView.as_view(),
        name="lista_detail_clientes",
    ),
    path(
        "delete_clientes/<int:pk>",
        views.ClienteDeleteView.as_view(),
        name="delete_clientes",
    ),
]
