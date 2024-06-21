# O que é Django Template Language?

O Django Template Language (DTL) é o Template Engine padrão do Django, responsável por criar páginas HTML em projetos com o framework.

Escrito em Python, o DTL tem como objetivo auxiliar na criação de páginas HTML em aplicações Django. Basicamente, ele serve para permitir que as informações trocadas entre uma aplicação escrita em Django e suas páginas HTML sejam feitas de forma mais simples e intuitiva.

Desta forma, garante ao desenvolvedor que a criação de templates para suas aplicações sejam feitas de forma mais rápida. É um template engine projetado para encontrar o “equilíbrio” entre poder e facilidade, sendo de fácil aprendizagem aos desenvolvedores que já possuírem facilidade em trabalhar com o HTML ou com outros templates engines, como o Jinja2 ou o Smarty.

# Você sabe o que é um Template Engine?

Basicamente, uma template engine serve para facilitar a criação de páginas HTML e tornar o envio e exibição de informações para estas páginas um processo mais simples e organizado.

Traz como vantagens, se comparada ao uso de HTML puro, as seguintes características:

- Maior velocidade na criação de templates;
- Melhor reaproveitamento de código HTML;
- Uso de tipos de dados nativos em páginas HTML;
- Uso de recursos das linguagens de programação em páginas HTML (estruturas de condição, repetição, etc), entre outros.
- Desta forma, com o seu uso, podemos utilizar recursos das linguagens de desenvolvimento para criar páginas HTML, como estruturas de condição, estruturas de repetição, herança, etc, facilitando a criação da camada de visualização de dados em uma aplicação.

# Características do Django Template Language

Conforme vimos no tópico anterior, uma template engine facilita para que linguagens de programação sejam incorporadas em páginas HTML.

Desta forma, ao utilizar o DTL podemos facilmente incorporar códigos Python de aplicações Django em templates HTML.

Como principais características podemos citar:

- Permite a criação de filtros para transformar o conteúdo de - - variáveis exibidas nos templates;
- Com o Django Template Language é possível incluir tags para - melhorar a estrutura das páginas HTML da aplicação;
- Permite reaproveitar páginas HTML de diferentes templates e assim melhorar a reusabilidade do código;
- Permite utilizar estruturas de condição e repetição em páginas HTML, entre outros.

# Exemplo de uma página HTML com o Django Template Language

```
{% extends "base_generic.html" %}

{% block title %}{{ section.title }}{% endblock %}

{% block content %}
<h1>{{ section.title }}</h1>

{% for story in story_list %}
<h2>
  <a href="{{ story.get_absolute_url }}">
    {{ story.headline|upper }}
  </a>
</h2>
<p>{{ story.tease|truncatewords:"100" }}</p>
{% endfor %}
{% endblock %}

 ```

 Como podemos verificar o código acima, o Django Template Language permite utilizar diferentes recursos em páginas HTML, como a herança (extends), blocos de conteúdo (block), estruturas de repetição (for) e filtros (upper e truncatewords), garantindo um poder muito maior para a criação de páginas web.

 # Podemos então concluir…

 Como podemos acompanhar durante todo o artigo, o Django Template Language fornece meios para que as páginas HTML desenvolvidas em projetos Django sejam mais simples de desenvolver e com recursos muito mais avançados, quando comparados ao HTML puro.

Toda a documentação do Django Template Language pode ser acessada na própria documentação do Django na sessão do Django Template Language.
