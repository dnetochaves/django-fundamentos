from django.urls import path
from . import views 

urlpatterns = [
    path("clientes", views.clientes),
    path("clientes_form", views.ClienteCreateView.as_view()),
    path("clientes_list", views.ClienteListView.as_view(), name="clientes_list"),
    path("clientes_update/<int:pk>", views.ClienteUpdateView.as_view(), name="clientes_update"),
]
