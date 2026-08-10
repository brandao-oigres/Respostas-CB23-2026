import unittest
from P06_3489_pilha_encadeada import PilhaEncadeada
from P06_3489_fila_encadeada import FilaEncadeada

class TestPilhaEncadeada(unittest.TestCase):

    def setUp(self):
        self.pilha = PilhaEncadeada()

    # 1. Ordem LIFO em sequência de push/pop
    def test_LIFO(self):
        self.pilha.push(1)
        self.pilha.push(2)
        self.pilha.push(3)
        self.assertEqual(self.pilha.pop(), 3)
        self.assertEqual(self.pilha.pop(), 2)
        self.assertEqual(self.pilha.pop(), 1)

    # 2. pop e topo em pilha vazia
    def test_pop_topo_vazio(self):
        with self.assertRaises(IndexError):
            self.pilha.pop()

        with self.assertRaises(IndexError):
            self.pilha.topo()

    # 3. coerência de len após inserções e remoções
    def test_len(self):
        self.assertEqual(self.pilha.len(), 0)
        self.pilha.push(1)
        self.assertEqual(self.pilha.len(), 1)
        self.pilha.push(1)
        self.assertEqual(self.pilha.len(), 2)
        self.pilha.pop()
        self.assertEqual(self.pilha.len(), 1)
        self.pilha.pop()
        self.assertEqual(self.pilha.len(), 0)
        self.pilha.push(1)
        self.assertEqual(self.pilha.len(), 1)
        self.pilha.pop()
        self.assertEqual(self.pilha.len(), 0)

    # 4. alternância de operações
    def test_alternado(self):
        self.pilha.push(1)
        self.assertEqual(self.pilha.pop(), 1)
        self.assertEqual(self.pilha.len(), 0)
        with self.assertRaises(IndexError):
            self.pilha.pop()
        self.pilha.push(2)
        self.assertEqual(self.pilha.pop(), 2)
        self.pilha.push(3)
        self.assertEqual(self.pilha.len(), 1)
        self.assertEqual(self.pilha.pop(), 3)
        self.assertTrue(self.pilha.esta_vazia())

    # 5. armazenamento de itens de tipos diferentes, incluindo valores repetidos e None
    def test_armazenameto(self):
        self.pilha.push("str") #str
        self.pilha.push(True) #bool
        self.pilha.push(2) #int
        self.pilha.push(3.1415) #float
        self.pilha.push([1,1,2,3,5,8,13,21]) #lista
        self.pilha.push(set([1,2,3,4,5,6,7,8])) #conjunto
        self.pilha.push({"Dicionario":"substantivo: livro que lista palavras e seus significados."}) #dicionario
        self.pilha.push(2) #int e repetido
        self.pilha.push() #None por padrão
        self.pilha.push(None) #None (de certo modo, repetido)
        self.assertEqual(self.pilha.pop(), None)
        self.assertEqual(self.pilha.pop(), None)
        self.assertEqual(self.pilha.pop(), 2)
        self.assertEqual(self.pilha.pop(), {"Dicionario":"substantivo: livro que lista palavras e seus significados."})
        self.assertEqual(self.pilha.pop(), set([1,2,3,4,5,6,7,8]))
        self.assertEqual(self.pilha.pop(), [1,1,2,3,5,8,13,21])
        self.assertEqual(self.pilha.pop(), 3.1415)
        self.assertEqual(self.pilha.pop(), 2)
        self.assertEqual(self.pilha.pop(), True)
        self.assertEqual(self.pilha.pop(), "str")

class TestFilaEncadeada(unittest.TestCase):

    def setUp(self):
        self.fila = FilaEncadeada()

    # 1. Ordem FIFO 
    def test_FIFO(self):
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        self.fila.enfileirar(3)
        self.assertEqual(self.fila.desenfileirar(), 1)
        self.assertEqual(self.fila.desenfileirar(), 2)
        self.assertEqual(self.fila.desenfileirar(), 3)

    # 2. intercalação de enfileirar e desenfileirar
    def test_intercalado(self):
        self.fila.enfileirar("str") #str
        self.fila.enfileirar(True) #bool
        self.fila.enfileirar(2) #int
        self.assertEqual(self.fila.desenfileirar(), "str")
        self.fila.enfileirar(3.1415) #float
        self.assertEqual(self.fila.desenfileirar(), True)
        self.fila.enfileirar([1,1,2,3,5,8,13,21]) #lista
        self.assertEqual(self.fila.desenfileirar(), 2)
        self.assertEqual(self.fila.desenfileirar(), 3.1415)
        self.fila.enfileirar(set([1,2,3,4,5,6,7,8])) #conjuntoenfileirar
        self.assertEqual(self.fila.desenfileirar(), [1,1,2,3,5,8,13,21])
        self.fila.enfileirar({"Dicionario":"substantivo: livro que lista palavras e seus significados."}) #dicionario
        self.assertEqual(self.fila.desenfileirar(), set([1,2,3,4,5,6,7,8]))
        self.fila.enfileirar(2) #int e repetido
        self.assertEqual(self.fila.desenfileirar(), {"Dicionario":"substantivo: livro que lista palavras e seus significados."})
        self.fila.enfileirar() #None por padrão
        self.assertEqual(self.fila.desenfileirar(), 2)
        self.fila.enfileirar(None) #None (de certo modo, repetido)
        self.assertEqual(self.fila.desenfileirar(), None)
        self.assertEqual(self.fila.desenfileirar(), None)
        
    # 3. esvaziar e voltar a usar a mesma instância
    def test_esvaziar_usar_mesma_instancia(self):
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        self.assertFalse(self.fila.esta_vazia())
        self.fila.desenfileirar()
        self.fila.desenfileirar()
        self.assertTrue(self.fila.esta_vazia())
        self.fila.enfileirar(3)
        self.assertFalse(self.fila.esta_vazia())
        self.assertEqual(self.fila.frente(), 3)
        self.assertEqual(self.fila.desenfileirar(), 3)


    # 4. desenfileirar e frente em fila vazia
    def test_desenfileirar_frente_vazia(self):
        with self.assertRaises(IndexError):
                    self.fila.desenfileirar()
        
        with self.assertRaises(IndexError):
                    self.fila.frente()
        

    # 5. coerência de len
    def test_len(self):
        self.fila.enfileirar(1)
        self.assertEqual(self.fila.desenfileirar(), 1)
        self.assertEqual(self.fila.len(), 0)
        with self.assertRaises(IndexError):
            self.fila.desenfileirar()
        self.fila.enfileirar(2)
        self.assertEqual(self.fila.desenfileirar(), 2)
        self.fila.enfileirar(3)
        self.assertEqual(self.fila.len(), 1)
        self.assertEqual(self.fila.desenfileirar(), 3)
        self.assertTrue(self.fila.esta_vazia())

        
if __name__ == '__main__':
    unittest.main()