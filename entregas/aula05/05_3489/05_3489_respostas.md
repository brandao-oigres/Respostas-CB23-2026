# Questão 1:
Os Funcionários pode herdar de Pessoa, pois todo funcionário deve ter os atributos nome e idade. Sendo, pois, Funcionário a subclasse e Pessoa a classe base. Garçom, Chefe de cozinha e Gerente podem ser subclasses de Funcionário, pois, assim, herdaria os atributos de Funcionário (salario e carga_horarioa) e de Pessoa (nome e idade).

Iguaria pode ser uma classe primária, onde Pizza e Bolo são subclasses, ou seja, Pizza e Bolo herdariam os atributos nome e preço.

Pizzaria é um tipo de restaurante, portanto, podemos dizer que, nesse caso, Restaurante é a classe base e Pizzaria a subclasse. Pizzaria herdaria de restaurante os atributos nome, endereço e telefone.

# Questão 2:
As iguarias podem ser adicionadas e removidas do cardárpio do restaurante. Para tanto, adicionaremos a classe Cardápio com as funções de adicionar e remover iguarias. 

# Questão 3:
anotar_pedido pode receber como argumento1 uma lista de instâncias da classe Iguaria. Cada elemento da lista deve ser uma Iguaria a qual possui os atributos gerais (da Classe Iguaria(comida)) e específicos (como no caso que for pizza, haverá a informação se deve haver borda recheada).

preparar pode aceitar como argumento2 a lista de instâncias da classe Iguaria guardada ao utilizar o método anotar_pedido pois o Chefe de cozinha deve preparar o pedido anotado.


demitir pode receber o argumento3 sendo a instância de classe Funcionario, pois então ele terá acesso aos dados do funcionário enquanto Pessoa (nome e idade) e enquanto Funcionário (salário e carga_horaria), para saber quem demitir e as consequências disso na empresa.