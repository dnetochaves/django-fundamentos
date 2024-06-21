from django import template

register = template.Library()


@register.filter("remover_caracter")
def remover_caracter(var, caracter):
    return var.replace(caracter, "")
