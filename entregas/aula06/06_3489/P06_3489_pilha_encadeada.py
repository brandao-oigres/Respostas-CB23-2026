#Pilha_Encadeada
class PilhaEncadeada:

    class _No:
        """Cria a classe _No para atribuir um valor "valor" e um ponteiro "abaixo"
        """
        def __init__(self,valor, abaixo = None):
            """
            """
            self.valor = valor
            self.abaixo = abaixo

    def __init__(self):
        """... e inicia um contador no zero.
        """
        self.apice = None
        self.cont = 0

    def push(self, item = None):
        """Cria uma variável chamada "novo_apice" que aponta para o No feito com o valor do item e com o ponteiro apontando para o antigo apice "self.apice".
        É atribuído, caso o usuário não insira algum valor a item, item = None.
        Além de aumentar o contador em 1. Tudo com complexidade O(1), pois o número de operações feitas independe de alguma entrada.
        """
        novo_apice = self._No(item, self.apice)
        self.apice = novo_apice
        self.cont += 1

    def pop(self):
        """ Se o contador estiver zerado indica que a pilha está vazia, logo retorna IndexError com um aviso. No contrário, o é atribuido "self.apice.abaixo" (o No abaixo) ao "self.apice."
        Além de diminuir o contador em 1 caso a lista não esteja vazia inicialmente. Se o item for removido, retorna-se ele. Tudo com complexidade O(1), pois o número de operações feitas independe de alguma entrada.
        """
        if self.cont==0:
            raise IndexError("Não foi possível remover nenhum item, pois a pilha está vazia.") #verificar
        retorno = self.apice.valor
        self.apice = self.apice.abaixo
        self.cont-=1
        return retorno

    def topo(self):
        """Se o "self.apice" for None, então a lista está vazia e retorna IndexError com um aviso. Caso a lista não esteja vazia, retorna o valor do No do apice: "self.apice.valor."
        Tudo com complexidade O(1), pois o número de operações feitas independe de alguma entrada.
        """
        if self.apice == None:
           raise IndexError("Não foi exibir o topo da pilha, pois ela está vazia.") #verificar
        return self.apice.valor

    def esta_vazia(self):
        """Se o contador estiver zerado, então a lista está vazia e retorna True. Caso contrário retorna False.
        Tudo com complexidade O(1), pois o número de operações feitas independe de alguma entrada.
        """
        if self.cont == 0:
            return True
        return False

    def len(self):
        """Retorna o contador que indica o tamanho da pilha.
        Tudo com complexidade O(1), pois o número de operações feitas independe de alguma entrada.
        """
        return self.cont

    def repr(self):
        """Este método cria uma string j incialmente e percorre toda a pilha adicionando o valor (em formato de string) de algum item da pilha e a string " → " entre os valores a string j inicial.
        Tudo com complexidade O(N), pois como percorre toda a lista de modo linear, a complexidade depende do tamanho N da lista linearmente.
        """
        retorno = ""
        saida = self.apice
        for i in range(self.cont):
            if i < self.cont - 1:
                retorno += str(saida.valor)
                retorno +=  " → "
                saida = saida.abaixo
            else:
                retorno += str(saida.valor)
                
        return retorno
