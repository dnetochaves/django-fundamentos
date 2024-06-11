# O que é HTTP, Request, GET, POST, Response, 200, 404?


Aprenda nesse post de forma simples e direta os principais conceitos HTTP que sempre teve dúvida, porém nunca teve coragem de perguntar.

Nosso objetivo nesse post não é entrar 100% na parte técnica do protocolo HTTP, mas sim apresentar uma visão prática dele. Caso tenha interesse em se aprofundar aconselho dar uma olhada no nosso curso específico:

Antes de falar sobre conceitos que fazem parte do HTTP, precisamos entender o que é o HTTP em si.

# O que é HTTP

O HTTP é um protocolo de comunicação. Através dele o cliente e o servidor conseguem se comunicar, seguindo um conjunto de regras bem definidas (por isso chamamos de protocolo). Por exemplo, se estivermos falando de uma aplicação web, o cliente é o navegador, ele envia um pedido para o servidor web usando o protocolo HTTP, com base nesse pedido, se tudo estiver correto, o servidor responde também usando o mesmo protocolo o conteúdo solicitado.

# O que é Request

A Request ou requisição traduzindo diretamente para português, é o pedido que um cliente realiza a nosso servidor. Esse pedido contém uma série de dados que são usados para descrever exatamente o que o cliente precisa. Vamos pensar que um cliente precisa cadastrar um novo produto, ele deve passar todos os dados necessários para o cadastro acontecer de maneira correta, inclusive os dados que foram digitados pelo usuário em um formulário, no caso de uma aplicação web. No navegador toda vez que trocamos de página ou apertamos enter na barra de endereço uma nova request é feita. Independente se estamos apenas pedindo a exibição de uma página, cadastrando um novo recurso, atualizando ou excluindo.

# O que é GET e POST?

Tanto GET como POST na verdade são métodos HTTP. Eles indicam para o servidor qual a ação que o cliente deseja realizar. Quando realizamos uma requisição obrigatoriamente precisamos informar um método.

* GET – é usado quando o cliente deseja obter recursos do servidor*

* POST – é usado quando o cliente deseja enviar dados para processamento ao servidor, como os dados de um formulário, por exemplo.
Existem outros métodos HTTP. Os dois métodos citados acima são os mais usados, principalmente em aplicações web. Quando o usuário digita um endereço e aperta enter na barra de endereço do navegador, ele realiza uma requisição do tipo GET. Já quando preenchemos um formulário e clicamos em enviar geralmente o método usado é o POST.*

# O que é Response

Vimos que o cliente envia uma Request (requisição) ao servidor. Essa requisição possui todas as informações acerca do que o cliente espera receber de volta. O servidor web ao receber essas informações precisa enviar uma resposta ao cliente, nesse ponto entra a Response. A Response (resposta) nada mais é do que a resposta que o servidor envia ao cliente. Essa resposta pode conter os dados que realmente o cliente esperava receber ou uma resposta informando que alguma coisa deu errado.

# O que é 200, 404, 301 e outros números?

Esses números são os chamados códigos HTTP. Quando o cliente faz uma requisição ele espera uma resposta. O servidor pode realmente responder o que o cliente esperava ou devolver outra informação, justamente nesse ponto entram os códigos HTTP. O servidor utiliza um código desse na resposta para indicar o que aconteceu.

Os códigos estão entre 100 e 500, sendo que cada centena indica uma categoria:

* 1xx – Informativos
* 2xx – Indicativos de sucesso
* 3xx – Redirecionamentos
* 4xx – Erros do cliente na hora de fazer a solicitação
* 5xx – Erros no lado do servidor

Dentro de cada centena temos os códigos específicos, por exemplo:

* 200 - Tudo ocorreu corretamente
* 301 – Indica redirecionamento permanente
* 401 – Não autorizado
* 404 – O recurso solicitado não foi encontrado no servidor

Existem vários sites que especificam todos os códigos HTTP. Esse usa cachorrinhos como exemplo , mas se você gosta mais dos gatinhos também existe.

# Resumo

O HTTP é o protocolo que define as regras para a comunicação entre o cliente o servidor. No fluxo básico o cliente realiza uma requisição para o servidor, nessa requisição é enviada além de várias outras informações um método que indica a ação que ele deseja. O servidor devolve uma resposta, nessa resposta, além de outras informações, existe um código que indica ao cliente o que aconteceu. Caso você queira se aprofundar no assunto também abordamos no blog sobre o protocolo HTTP/2, que é a evolução do HTTP.