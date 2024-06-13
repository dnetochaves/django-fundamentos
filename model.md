 * [Voltar](README.md)
 </hr>

## Para quê serve a camada Model?

Como vimos anteriormente, o Django é separado em três camadas principais (Model-Template-View). A camada Model tem um papel fundamental nessa arquitetura. É ela quem se comunica, através do ORM do Django, com o banco de dados para criar os modelos da aplicação diretamente no banco de dados sem a necessidade de usar código SQL.

Basicamente, a camada model é quem define como as entidades serão criadas no banco de dados do projeto, como podemos ver na figura abaixo:

![model.png](padrão-mtv.png "Hover text")