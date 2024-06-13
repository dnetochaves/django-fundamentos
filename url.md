 * [Voltar](README.md)
 </hr>
 
# Para quê servem as urls?

As rotas são de fundamental importância para que o usuário consiga executar determinada funcionalidade do sistema. No Django, cada rota é responsável por executar um método na view da aplicação, que exibe alguma informação para o usuário.

No Django, o processamento de rotas acontece da seguinte forma:

* 1 - Uma URL é invocada por meio do navegador;
* 2 - O Django captura a URL, verifica o método que esta rota executa e repassa a requisição para ela;
* 3 - A partir daí o restante da requisição é feita pelas outras camadas do Django.
Durante este curso veremos todas as funcionalidades do Django em detalhes.