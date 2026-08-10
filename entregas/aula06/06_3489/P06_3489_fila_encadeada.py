from P06_3489_pilha_encadeada import PilhaEncadeada

class FilaEncadeada():
    def __init__(self):
        self.entrada = PilhaEncadeada()
        self.saida = PilhaEncadeada()

    def enfileirar(self, item = None):
        """Adiciona o item a pilha de entrada com complexidade O(1).
        É atribuído, caso o usuário não insira algum valor a item, item = None.
        """
        self.entrada.push(item)

    def desenfileirar(self):
        """Retorna e remove o item do topo da pilha de saída caso essa não esteja vazia. 
        Caso contrário, verificamos se a pilha de entrada está vazia. 
        Se estiver, então retornamos IndexError.
        Se não, então passamos todos os itens da pilha de entrada para a pilha de saída de modo a inverter a ordem de entrada e retornarmos o item do topo da pilha de saída o removendo.
        Tudo isso em complexidade O(1) amortecido, pois não é sempre que teremos que transferir de uma pilha a outra, apenas quando somente a pilha de entrada conter itens.
        """
        if not self.saida.esta_vazia():
            return self.saida.pop()

        if self.entrada.esta_vazia():
            raise IndexError("Não é possível desenfileirar nada da fila, pois ela está vazia.")
        
        while not self.entrada.esta_vazia():
            self.saida.push(self.entrada.pop())
        return self.saida.pop()

    def frente(self):
        """Retorna o item do topo da pilha de saída caso essa não esteja vazia. 
        Caso contrário, verificamos se a pilha de entrada está vazia. 
        Se estiver, então retornamos IndexError.
        Se não, então passamos todos os itens da pilha de entrada para a pilha de saída de modo a inverter a ordem de entrada e retornarmos o item do topo da pilha de saída.
        Tudo isso em complexidade O(1) amortecido, pois não é sempre que teremos que transferir de uma pilha a outra, apenas quando somente a pilha de entrada conter itens.
        """
        if not self.saida.esta_vazia():
            return self.saida.topo()

        if self.entrada.esta_vazia():
            raise IndexError("Não é possível mostrar o primeiro item da fila, pois ela está vazia.")
        
        while not self.entrada.esta_vazia():
            self.saida.push(self.entrada.pop())
        return self.saida.topo()

    def esta_vazia(self):
        """Verifica-se se ambas as pilhas (a de entrada e a de saída) estão vazias. Se ambas estão, retorna-se True. Caso contrário retorna-se False.
        Tudo em complexidade O(1), pois basta realizar a operação de verificação em ambas as pilhas.
        """
        if self.saida.esta_vazia() and self.entrada.esta_vazia():
            return True
        return False

    def len(self):
        """Retorna-se a soma do tamanho da pilha de entrada e da pilha de saída. 
        Como medir o tamanho de pilhas é O(1), então medir o tamanho desta fila também é O(1)."""
        return self.saida.len() +self.entrada.len()

    def repr(self):
        """Criamos uma string de retorno e atribuimos o valor de self.saida.repr() a ela, se a pilha de entrada estiver vazia, retornamos essa string.
        Caso contrário, cria-se uma pilha auxiliar de entrada a qual colocamos todos os itens da pilha de entrada nela. 
        Concatenamos retorno com a aux_entrada.repr() e após isso colocamos item por item de volta na pilha de entrada e retornamos a string retorno.
        Tudo isso em complexidade O(N), pois a complexidade depende apenas do tamanho da fila de modo linear."""
        retorno = self.saida.repr()
        if self.entrada.esta_vazia():
            return retorno
        if not self.saida.esta_vazia():
            retorno +=  " → "
        aux_entrada = PilhaEncadeada()
        for _ in range(self.entrada.len()):
            aux_entrada.push(self.entrada.pop())
        retorno += aux_entrada.repr()
        for _ in range(aux_entrada.len()):
            self.entrada.push(aux_entrada.pop())
        return retorno        
        
        

