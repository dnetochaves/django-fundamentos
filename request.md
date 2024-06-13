 * [Voltar](README.md)
 </hr>
# Entendendo o parâmetro request

Quando uma requisição é enviada através do Django, a view recebe um objeto request. Este objeto é de grande importância pois é ele quem possui todos os metadados da requisição.

Estes metadados são dos mais variados, como:

* HttpRequest.scheme: Representa o tipo de requisição (http ou https);
* HttpRequest.path: Retorna o caminho completo da rota que foi executada anteriormente;
* HttpRequest.method: Retorna o método utilizado na requisição (GET, POST, PUT, PATCH, DELETE);
* HttpRequest.cookies: Um dicionário que contém todos os cookies da requisição.

Há diversos outros metadados que podem ser obtidos com o objeto request no Django. Todos eles podem ser vistos por meio da sua documentação oficial no seguinte link: https://docs.djangoproject.com/en/4.1/ref/request-response/#httprequest-objects