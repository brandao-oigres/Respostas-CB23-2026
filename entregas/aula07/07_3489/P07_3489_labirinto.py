import random

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    

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

def generate_maze(m, n, room=0, wall=1, cheese='.'):
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]
    pilha_criando = PilhaEncadeada()
    # Deslocamentos para os quatro vizinhos cardeais: N, S, W, E
    
    def dfs(x, y):
        """Abre passagens recursivamente a partir da sala (x, y)."""
        pilha_criando.push((x,y,random.sample(directions, len(directions))))
        maze[2 * x + 1][2 * y + 1] = room

        while not pilha_criando.esta_vazia():
            cx, cy, dirs = pilha_criando.topo()
            if not dirs:
                pilha_criando.pop()
                continue

            dx, dy = dirs.pop()
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                # Derruba a parede entre (x,y) e (nx,ny)
                maze[2 * cx + 1 + dx][2 * cy + 1 + dy] = room
                maze[2 * nx + 1][2 * ny + 1] = room

                pilha_criando.push((nx, ny, random.sample(directions, len(directions))))


    # Inicia a DFS no canto superior-esquerdo da grade lógica
    dfs(0, 0)

    # Posiciona o queijo em uma sala aleatória (rejeita paredes)
    while True:
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * m))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze


def print_maze(maze):
    """Imprime o labirinto no terminal, uma linha por vez.

    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    for row in maze:
        print(" ".join(map(str, row)))


def encontrar_caminho():
    if maze[1][1] == cheese:
        print_maze(maze)
        return 
    pilha = PilhaEncadeada()
    pilha.push((1,1,list(directions)))
    visitados = {(1,1)}
    caminho = [(1,1)]

    while not pilha.esta_vazia():
        cx, cy, dirs = pilha.topo()

        if not dirs:
            pilha.pop()
            caminho.pop()
            continue
        
        dx, dy = dirs.pop()
        nx, ny = cx + dx, cy + dy

        if maze[nx][ny] != wall and (nx, ny) not in visitados:
            if maze[nx][ny] == cheese:
                for cx, cy in caminho:
                    maze[cx][cy] = '⋅'
                print_maze(maze)
                return caminho
            visitados.add((nx, ny))
            caminho.append((nx,ny))
            pilha.push((nx,ny,list(directions)))
    
    

# Example usage:
if __name__ == '__main__':
    m, n = 10, 14  # Grid size
    random.seed(10110)
    maze = generate_maze(m, n)
    print('Maze 1')
    print_maze(maze)

    room = ' '
    wall = 'W'
    cheese = '*'
    maze = generate_maze(m, n, room, wall, cheese)
    print('\nMaze 2')
    print_maze(maze)
    print('\nMaze Caminho')
    encontrar_caminho()


