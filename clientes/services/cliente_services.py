def calcular_nivel_cliente(cliente):
    if cliente.profissao == "Programador":
        cliente.nivel = 1
    else:
        cliente.nivel = 2
    return cliente
