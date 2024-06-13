from django.urls import path
from . import views 

urlpatterns = [
    path("clientes", views.clientes),
    path("clientes_form", views.ClienteCreateView.as_view()),
]
