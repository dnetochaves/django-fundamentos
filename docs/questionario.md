# Como acessamos o valor de um atributo dentro de um dicionário em nossos templates?

- [ ] {{nome_do_dicionario_nome_do_atributo}}.
- [x] {{nome_do_dicionario_nome_do_atributo}}.
- [ ] {{nome_do_dicionario_nome_do_atributo}}.
- [ ] {{nome_do_dicionario_nome_do_atributo}}.
- [ ] {{nome_do_dicionario_nome_do_atributo}}.

<hr>

# Como fazemos para exibir informações de uma variável Python dentro de um template Django?

- [x] {{nome_da_variavel}}.
- [ ] ((nome_da_variavel)).
- [ ] {%nome_da_variavel%}.
- [ ] %%nome_da_variavel%%.
- [ ] {nome_da_variavel}.
<hr>

# Qual template tag utilizamos para criar blocos de comentários nos templates do Django?

- [ ] Conteúdo do comentário {% endcomment %}`.
- [x] {% comment %} Conteúdo do comentário {% endcomment %}.
- [ ] {% comment %} Conteúdo do comentário {% end %}.
- [ ] {% comment %} Conteúdo do comentário {% comment %}.
- [ ] {% comment %} Conteúdo do comentário.
<hr>

# Qual template tag utilizamos para criar rotas nos templates do Django?

- [ ] {% urls 'nome_da_rota' %}.
- [ ] {{ url 'nome_da_rota' }}.
- [ ] {% http 'nome_da_rota' %}.
- [x] {% url 'nome_da_rota' %}.
- [ ] {% route 'nome_da_rota' %}.
<hr>

# Observe o código abaixo?

```
# views.py
def index(request):
    nome_da_empresa = "TreinaWeb"
    descricao_da_empresa = "Há mais de 12 anos formando desenvolvedores de ponta! São mais de 4.000 horas de conteúdo, com formações completas e com foco no mercado de trabalho."


    cursos_home = {

    }

    return render(request, 'empresa/index.html', {'nome_empresa':nome_da_empresa, 'descricao_empresa':descricao_da_empresa,
                                                  'cursos_home':cursos_home})
-------------------
# index.html
<div class="row">
  {% for curso_id, curso in cursos_home.items %}
  <div class="col-md-4 mb-5">
    <div class="card h-100">
      <img class="card-img-top" src="http://placehold.it/300x200" alt="">
      <div class="card-body">
          <h4 class="card-title">{{curso_id}} - {{curso.titulo}}</h4>
        <p class="card-text">{{curso.descricao}}</p>
      </div>
      <div class="card-footer">
        <a href="#" class="btn btn-primary">Find Out More!</a>
      </div>
    </div>
  </div>
  {% empty %}
    <h3>Novos cursos serão lançados em breve</h3>
  {% endfor %}
</div>
```



- [ ] O que será impresso quando o arquivo index.html for renderizado?

- [x] A mensagem "Novos cursos serão lançados em breve".

- [ ] O titulo e descrição de todos os cursos.

- [ ] O titulo de todos os cursos.

- [ ] O id, titulo e descrição de todos os cursos.

- [ ] Nada, pois haverá um erro de execução no código.

- [ ] O id, e descrição de todos os cursos.
<hr>

# Qual template tag utilizamos para repetir um determinado bloco de código no sistema de templates do Django?

- [ ] {% loop %}.
- [ ] {% while %}.
- [ ] {% do while %}.
- [ ] {% forloop %}.
- [x] {% for %}.
<hr>

# Observe o código abaixo:



```
{% for curso_id, curso in cursos_home %}
<div class="col-md-4 mb-5">
  <div class="card h-100">
    <img class="card-img-top" src="http://placehold.it/300x200" alt="">
    <div class="card-body">
      <h4 class="card-title">{{curso_id}}</h4>
    </div>
    <div class="card-footer">
      <a href="#" class="btn btn-primary">Find Out More!</a>
    </div>
  </div>
</div>
{% endfor %}

```
Partindo do pressuposto que a variável cursos_home possui outros dicionários armazenados, o que será exibido após sua execução?

- [ ] Será exibido os ids dos cursos existentes no dicionário cursos_home.
- [x] Não será exibido nada, já que a forma que iteramos o dicionário cursos_home está incorreta.
- [ ] Será exibido os titulos dos cursos existentes no dicionário cursos_home.
- [ ] Será exibido os cursos existentes no dicionário cursos_home.
- [ ] Será exibido o id do primeiro curso existente no dicionário cursos_home.

<hr>

# Qual template tag utilzamos para criar uma execução condicional no sistema de template do Django?

- [x] {% if %}.
- [ ] {% if_django %}.
- [ ] {% case %}.
- [ ] {% switch %}.
- [ ] {% conditional %}.
- [ ] {% else %}.
<hr>

# Qual template tag utilzamos para não exibir dados imediatamente iguais no DTL?

- [ ] {% case %}.
- [ ] {% switch %}.
- [X] {% ifchanged %}.
- [ ] {% else %}.
- [ ] {% if_django %}.
- [ ] {% conditional %}.
<hr>

# Qual sintaxe utilizada para o uso de filtros no Django Templates?

- [x] {{nome_da_variavel|nome_do_filtro}}.
- [ ] {{nome_do_filtro|nome_da_variavel}}.
- [ ] {{nome_da_variavel/nome_do_filtro}}.
- [ ] {{nome_da_variavel?nome_do_filtro}}.
- [ ] {% if_django %}.
- [ ] {{nome_da_variavel:nome_do_filtro}}.
<hr>

# Qual filtro utilizado para transformar todos os caracteres de uma palavra (ou frase) em maiúsculo?

- [ ] maiusculum.
- [ ] upp.
- [x] upper.
- [ ] size.
- [ ] lower.
<hr>

# Qual o nome do diretório padrão que o Django usa para armazenar arquivos estáticos em seu projeto?

- [ ] static_files/.
- [ ] files_static/.
- [x] static/.
- [ ] css_js/.
- [ ] files/.
<hr>

# Caso a estrutura dos diretórios que armazenam os arquivos estáticos de um projeto esteja da seguinte maneira: /static/arquivos/css, como devemos usar a tag static em nossos templates?

- [ ] {% static 'arquivos/css/nome_do_arquivo.css' %}.
- [x] O Django não encontrará o arquivo, já que a estrutura do diretório static está incorreta.
- [ ] {% static 'app/css/nome_do_arquivo.css' %}.
- [ ] {% static 'app/arquivos/nome_do_arquivo.css' %}.
- [ ] {% static 'app/css/nome_do_arquivo.css' %}.
<hr>

# Qual tag utilizamos para que o Django reconheça o diretório static em nossos templates?

- [ ] {% static %}.
- [ ] {% load files %}.
- [x] {% load static %}.
- [ ] {% load static_files %}.
- [ ] {% load stati %}.
<hr>



# Qual template tag utilizada para herdar todo o conteúdo de uma página HTML em outro template?

- [ ] {% register "localizacao_do_template/nome_do_template.html" %}.
- [ ] {% use "localizacao_do_template/nome_do_template.html" %}
- [ ] {% herds "localizacao_do_template/nome_do_template.html" %}.
- [ ] {% include "localizacao_do_template/nome_do_template.html" %}.
- [x] {% extends "localizacao_do_template/nome_do_template.html" %}.
<hr>

# Qual template tag utilizada para criar blocos que receberão o código HTML das páginas que herdarão do arquivo base?

- [ ] {% blo %}.
- [ ] {% content %}.
- [x] {% block %}.
- [ ] {% bloco %}.
- [ ] {% conteudo %}.
<hr>

# Qual comando responsável por compilar os arquivos de tradução no Django?

- [ ] python manage.py makemessages.  
- [ ] django-admin compilemessages.
- [ ] manage.py compilemessages.
- [x] python manage.py compilemessages.
- [ ] python compilemessages.
<hr>

# Após configurar a aplicação para alterar seu idioma em tempo de execução, o que acontece se passarmos um idioma que não está configurado?

- [x] A aplicação exibirá um erro indicando que o idioma não existe.
- [ ] A aplicação será executada com o idioma padrão, definido no arquivo settings.py.
- [ ] A aplicação exibirá um erro indicando que a rota não existe.
- [ ] O servidor será reiniciado.
- [ ] A aplicação será executada com o último idioma selecionado.
<hr>

# Qual configuração devemos indicar onde os arquivos de tradução será armazenado?

- [ ] LOCALE, no arquivo settings.py.
- [ ] LOCALE_PATHS, no arquivo views.py.
- [ ] PATHS, no arquivo models.py.
- [x] LOCALE_PATHS, no arquivo settings.py.
- [ ] PATHS, no arquivo settings.py.
<hr>

# Como acessamos o valor de um atributo dentro de um dicionário em nossos templates?

- [ ] {{nome_do_dicionario_nome_do_atributo}}.
- [x] {{nome_do_dicionario_nome_do_atributo}}.
- [ ] {{nome_do_dicionario_nome_do_atributo}}.
- [ ] {{nome_do_dicionario_nome_do_atributo}}.
- [ ] {{nome_do_dicionario_nome_do_atributo}}.

<hr>

# Como fazemos para exibir informações de uma variável Python dentro de um template Django?

- [x] {{nome_da_variavel}}.
- [ ] ((nome_da_variavel)).
- [ ] {%nome_da_variavel%}.
- [ ] %%nome_da_variavel%%.
- [ ] {nome_da_variavel}.
<hr>

# Qual template tag utilizamos para criar blocos de comentários nos templates do Django?

- [ ] Conteúdo do comentário {% endcomment %}`.
- [x] {% comment %} Conteúdo do comentário {% endcomment %}.
- [ ] {% comment %} Conteúdo do comentário {% end %}.
- [ ] {% comment %} Conteúdo do comentário {% comment %}.
- [ ] {% comment %} Conteúdo do comentário.
<hr>

# Qual template tag utilizamos para criar rotas nos templates do Django?

- [ ] {% urls 'nome_da_rota' %}.
- [ ] {{ url 'nome_da_rota' }}.
- [ ] {% http 'nome_da_rota' %}.
- [x] {% url 'nome_da_rota' %}.
- [ ] {% route 'nome_da_rota' %}.
<hr>

# Observe o código abaixo?

```
# views.py
def index(request):
    nome_da_empresa = "TreinaWeb"
    descricao_da_empresa = "Há mais de 12 anos formando desenvolvedores de ponta! São mais de 4.000 horas de conteúdo, com formações completas e com foco no mercado de trabalho."


    cursos_home = {

    }

    return render(request, 'empresa/index.html', {'nome_empresa':nome_da_empresa, 'descricao_empresa':descricao_da_empresa,
                                                  'cursos_home':cursos_home})
-------------------
# index.html
<div class="row">
  {% for curso_id, curso in cursos_home.items %}
  <div class="col-md-4 mb-5">
    <div class="card h-100">
      <img class="card-img-top" src="http://placehold.it/300x200" alt="">
      <div class="card-body">
          <h4 class="card-title">{{curso_id}} - {{curso.titulo}}</h4>
        <p class="card-text">{{curso.descricao}}</p>
      </div>
      <div class="card-footer">
        <a href="#" class="btn btn-primary">Find Out More!</a>
      </div>
    </div>
  </div>
  {% empty %}
    <h3>Novos cursos serão lançados em breve</h3>
  {% endfor %}
</div>
```



- [ ] O que será impresso quando o arquivo index.html for renderizado?

- [x] A mensagem "Novos cursos serão lançados em breve".

- [ ] O titulo e descrição de todos os cursos.

- [ ] O titulo de todos os cursos.

- [ ] O id, titulo e descrição de todos os cursos.

- [ ] Nada, pois haverá um erro de execução no código.

- [ ] O id, e descrição de todos os cursos.
<hr>

# Qual template tag utilizamos para repetir um determinado bloco de código no sistema de templates do Django?

- [ ] {% loop %}.
- [ ] {% while %}.
- [ ] {% do while %}.
- [ ] {% forloop %}.
- [x] {% for %}.
<hr>

# Observe o código abaixo:



```
{% for curso_id, curso in cursos_home %}
<div class="col-md-4 mb-5">
  <div class="card h-100">
    <img class="card-img-top" src="http://placehold.it/300x200" alt="">
    <div class="card-body">
      <h4 class="card-title">{{curso_id}}</h4>
    </div>
    <div class="card-footer">
      <a href="#" class="btn btn-primary">Find Out More!</a>
    </div>
  </div>
</div>
{% endfor %}

```
Partindo do pressuposto que a variável cursos_home possui outros dicionários armazenados, o que será exibido após sua execução?

- [ ] Será exibido os ids dos cursos existentes no dicionário cursos_home.
- [x] Não será exibido nada, já que a forma que iteramos o dicionário cursos_home está incorreta.
- [ ] Será exibido os titulos dos cursos existentes no dicionário cursos_home.
- [ ] Será exibido os cursos existentes no dicionário cursos_home.
- [ ] Será exibido o id do primeiro curso existente no dicionário cursos_home.

<hr>

# Qual template tag utilzamos para criar uma execução condicional no sistema de template do Django?

- [x] {% if %}.
- [ ] {% if_django %}.
- [ ] {% case %}.
- [ ] {% switch %}.
- [ ] {% conditional %}.
- [ ] {% else %}.
<hr>

# Qual template tag utilzamos para não exibir dados imediatamente iguais no DTL?

- [ ] {% case %}.
- [ ] {% switch %}.
- [X] {% ifchanged %}.
- [ ] {% else %}.
- [ ] {% if_django %}.
- [ ] {% conditional %}.
<hr>

# Qual sintaxe utilizada para o uso de filtros no Django Templates?

- [x] {{nome_da_variavel|nome_do_filtro}}.
- [ ] {{nome_do_filtro|nome_da_variavel}}.
- [ ] {{nome_da_variavel/nome_do_filtro}}.
- [ ] {{nome_da_variavel?nome_do_filtro}}.
- [ ] {% if_django %}.
- [ ] {{nome_da_variavel:nome_do_filtro}}.
<hr>

# Qual filtro utilizado para transformar todos os caracteres de uma palavra (ou frase) em maiúsculo?

- [ ] maiusculum.
- [ ] upp.
- [x] upper.
- [ ] size.
- [ ] lower.
<hr>

# Qual o nome do diretório padrão que o Django usa para armazenar arquivos estáticos em seu projeto?

- [ ] static_files/.
- [ ] files_static/.
- [x] static/.
- [ ] css_js/.
- [ ] files/.
<hr>

# Caso a estrutura dos diretórios que armazenam os arquivos estáticos de um projeto esteja da seguinte maneira: /static/arquivos/css, como devemos usar a tag static em nossos templates?

- [ ] {% static 'arquivos/css/nome_do_arquivo.css' %}.
- [x] O Django não encontrará o arquivo, já que a estrutura do diretório static está incorreta.
- [ ] {% static 'app/css/nome_do_arquivo.css' %}.
- [ ] {% static 'app/arquivos/nome_do_arquivo.css' %}.
- [ ] {% static 'app/css/nome_do_arquivo.css' %}.
<hr>

# Qual tag utilizamos para que o Django reconheça o diretório static em nossos templates?

- [ ] {% static %}.
- [ ] {% load files %}.
- [x] {% load static %}.
- [ ] {% load static_files %}.
- [ ] {% load stati %}.
<hr>



# Qual template tag utilizada para herdar todo o conteúdo de uma página HTML em outro template?

- [ ] {% register "localizacao_do_template/nome_do_template.html" %}.
- [ ] {% use "localizacao_do_template/nome_do_template.html" %}
- [ ] {% herds "localizacao_do_template/nome_do_template.html" %}.
- [ ] {% include "localizacao_do_template/nome_do_template.html" %}.
- [x] {% extends "localizacao_do_template/nome_do_template.html" %}.
<hr>

# Qual template tag utilizada para criar blocos que receberão o código HTML das páginas que herdarão do arquivo base?

- [ ] {% blo %}.
- [ ] {% content %}.
- [x] {% block %}.
- [ ] {% bloco %}.
- [ ] {% conteudo %}.
<hr>

# Qual comando responsável por compilar os arquivos de tradução no Django?

- [ ] python manage.py makemessages.  
- [ ] django-admin compilemessages.
- [ ] manage.py compilemessages.
- [x] python manage.py compilemessages.
- [ ] python compilemessages.
<hr>

# Após configurar a aplicação para alterar seu idioma em tempo de execução, o que acontece se passarmos um idioma que não está configurado?

- [x] A aplicação exibirá um erro indicando que o idioma não existe.
- [ ] A aplicação será executada com o idioma padrão, definido no arquivo settings.py.
- [ ] A aplicação exibirá um erro indicando que a rota não existe.
- [ ] O servidor será reiniciado.
- [ ] A aplicação será executada com o último idioma selecionado.
<hr>

# Qual configuração devemos indicar onde os arquivos de tradução será armazenado?

- [ ] LOCALE, no arquivo settings.py.
- [ ] LOCALE_PATHS, no arquivo views.py.
- [ ] PATHS, no arquivo models.py.
- [x] LOCALE_PATHS, no arquivo settings.py.
- [ ] PATHS, no arquivo settings.py.
<hr>

# Com o relacionamento 1-1 entre as entidades Cliente e Endereço funcionando, como podemos exibir o nome da rua do endereço de um cliente em nosso template Django?

- [ ] {{cliente.rua}}.
- [ ] {{endereco.rua}}.
- [ ] {{cliente.endereco.rua}}.
- [x] {{cliente.endereco.rua.nome}}.
- [ ] {{cliente.endereco}}.
<hr>

# Dado as tabelas Cliente e Endereço, onde um relacionamento 1-1 exista entre elas, onde 1 cliente só pode possuir 1 endereço e 1 endereço só pode estar associado a 1 cliente e essa relação esteja armazenada na tabela Cliente, como fica, a nível de banco de dados, essa relação?

- [ ] Um campo endereco_id_cliente será criado na tabela Cliente.
- [ ] Um campo cliente_id será criado na tabela Endereço.
- [ ] Um campo endereco_id será criado na tabela Cliente.
- [x] Um campo cliente_id_endereco será criado na tabela Endereço.
- [ ] Um campo cliente_id_endereco será criado na tabela Endereço.
<hr>

# Qual método devemos sobrescrever no model para alterar a forma como um objeto é exibido através do ORM do Django?

- [x] __str__.
- [ ] get.
- [ ] __print__.
- [ ] print.
- [ ] str.
<hr>

# Dado as tabelas Cliente e Pedido, onde um relacionamento 1-N exista entre elas, onde 1 cliente pode realizar vários pedidos, porém 1 pedido só pode estar atrelado a 1 cliente, como fica, a nível de banco de dados, essa relação?

- [x] Um campo cliente_id_pedido será criado na tabela Pedido.
- [ ] Um campo cliente_id será criado na tabela Pedido.
- [ ] Uma tabela ClientePedido será criada para armazenar a relação.
- [ ] Um campo pedido_id será criado na tabela Cliente.
- [ ] Um campo pedido_id_cliente será criado na tabela Cliente. 
<hr>

# Qual o nome do campo do ORM do Django responsável por criar um relacionamento NN entre duas entidades?

- [x] ManyToManyField.
- [ ] ForeignKey.
- [ ] NtoNField.
- [ ] ManyToNField.
- [ ] NToManyField.
<hr>

# Observe o model Pedido abaixo:
```
class Pedido(models.Model):
    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para entrega"),
    )
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(default=timezone.now)
    valor = models.FloatField(blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)
    observacoes = models.CharField(max_length=50, null=True, blank=True)
    produtos = models.ManyToManyField(Produto)

```

## Com o campo "produtos" sendo um relacionamento N-N, qual o nome da tabela "auxiliar" que será criada no BD para armazenar as relações entre as duas entidades?
- [ ] nome_da_app_produtos_pedido.
- [ ] nome_da_app_pedidos_produtos.
- [ ] nome_da_app_pedidos_produto.
- [x] nome_da_app_pedido_produtos.
- [ ] nome_da_app_pedido_produto.
<hr>

## Qual método utilizado para recuperar elementos de uma relação NN no Django?
- [ ] many_related.
- [ ] select_related.
- [ ] related.
- [x] prefetch_related.
- [ ] A relação NN não precisa de um método específico.
<hr>  

## Supondo que a entidade Pedido se relaciona de forma NN com a entidade Produto, com base na query abaixo:

```
pedidos = Pedido.objects.prefetch_related('produtos').all()
```

Quantas consultas seriam realizadas para obter todos os dados da relação, supondo que temos 230 registros?


- [ ] 3 consultas.
- [ ] 1 consulta.
- [ ] 231 consultas.
- [x] 2 consultas.
- [ ] 30 consultas.
<hr>  


## Qual método utilizado para recuperar os elementos de uma relação 1N no Django?




- [ ] related`.
- [ ] A relação 1N não precisa de um método específico.
- [ ] A relação 1N não precisa de um método específico.
- [x] select_related`.
- [ ] many_related`.
<hr>  

## Qual classe devemos herdar para adicionar mais campos ao form de edição de usuário?


- [ ] UserUpdateForm.
- [x] UserChangeForm.
- [ ] ChangeForm.
- [ ] UserCreationForm.
- [ ] UserForm.
<hr>  

## Qual classe devemos herdar para adicionar mais campos ao form de cadastro de usuário?


- [ ] UserForm.
- [ ] UserNewForm.
- [x] UserCreationForm.
- [ ] Nenhuma das alterantivas.
- [ ] CreationForm.
<hr>  

## Qual o nome do modelo padrão de autenticação do Django?


- [ ] Usuario.
- [x] User.
- [ ] DjangoUser.
- [ ] Protect.
- [ ] Auth.
<hr>  