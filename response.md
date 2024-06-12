# Entendendo o parâmetro response

Assim como toda view recebe um objeto do tipo request como parâmetro, ela é obrigada a retornar um objeto response. Diferente do request que é criado automaticamente pelo Django, o response é de responsabilidade do programador.

Basicamente sua função é retornar alguma informação para o usuário, seja uma lista de usuários cadastrados ou uma mensagem de erro. Qualquer informação que deva ser passada da view para o template utiliza o response.

Todos os recursos do objeto response podem ser vistos através da documentação do Django no seguinte link: https://docs.djangoproject.com/en/4.1/ref/request-response/#httpresponse-objects