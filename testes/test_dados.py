"""Seus testes do Marco 1 (veja a seção 6 do ENUNCIADO_MARCO1.md).

Regras: pelo menos 8 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual ou np.allclose.
"""
import unittest

from elevatoria.dados import por_tag, ler_log


class TestPorTagExemplo(unittest.TestCase):
    """Exemplo do formato. `por_tag` é código existente da base."""

    def test_lista_vazia(self):
        """Sem registros, por_tag devolve uma lista vazia."""
        self.assertEqual(por_tag([], "PT101"), [])


# Acrescente abaixo as suas classes de teste, começando pelos testes de regressão da
# issue #4 (escreva-os ANTES de corrigir o defeito e confirme que falham).

class TestLerLog(unittest.TestCase):
    """Regras de contrato de ler_log"""

    def test_data_impossivel(self):
        """Dia 32 está no padrão, mas o strptime falha: a linha é inválida."""
        linha = "2026-10-32 08:00:00 INFO PT101 contagens=1"
        registros, invalidas = ler_log(linha + "\n")
        self.assertEqual((registros, invalidas), ([], [linha]))

    def test_resto_sem_par(self):
        """Linha sem chave=valor é considerada inválida."""
        linha = "2026-10-05 09:00:00 INFO PT101 sem_par_aqui"
        registros, invalidas = ler_log(linha + "\n")
        self.assertEqual((registros, invalidas), ([], [linha]))

    def test_linhas_vazias(self):
        """Linhas vazias são ignoradas."""
        texto = "\n   \n2026-10-05 10:00:00 INFO PT101 contagens=1\n\n"
        registros, invalidas = ler_log(texto)
        self.assertEqual(len(registros), 1)
        self.assertEqual(invalidas, [])
    
        



if __name__ == "__main__":
    unittest.main()
