from django.urls import path
from . import views

urlpatterns = [
    path("horario_atual", views.horario_atual),
    path("form_cliente", views.exibir_template),
]
