import unittest
from P06_3462_pilha_encadeada import PilhaEncadeada
from P06_3462_fila_encadeada import FilaEncadeada

class TestPilhaEncadeada(unittest.TestCase):

    def setUp(self):
        self.pilha = PilhaEncadeada()

    def test_pilha_inicial_vazia(self):
        self.assertTrue(self.pilha.esta_vazia())
        self.assertEqual(len(self.pilha), 0)

    def test_ordem_lifo(self):
        elementos = [10, "Python", 3.14, None, True]
        for elem in elementos:
            self.pilha.push(elem)

        for elem in reversed(elementos):
            self.assertEqual(self.pilha.pop(), elem)

    def test_excecao_pop_pilha_vazia(self):
        with self.assertRaises(IndexError):
            self.pilha.pop()

    def test_topo_sem_remover(self):
        self.pilha.push("A")
        self.pilha.push("B")
        self.assertEqual(self.pilha.topo(), "B")
        self.assertEqual(len(self.pilha), 2)

    def test_excecao_topo_pilha_vazia(self):
        with self.assertRaises(IndexError):
            self.pilha.topo()

    def test_coerencia_contador_len(self):
        for i in range(1, 6):
            self.pilha.push(i)
            self.assertEqual(len(self.pilha), i)

        for i in range(5, 0, -1):
            self.assertEqual(len(self.pilha), i)
            self.pilha.pop()

        self.assertEqual(len(self.pilha), 0)

    def test_representacao_repr(self):
        self.pilha.push(1)
        self.pilha.push(2)
        self.pilha.push(3)
        self.assertEqual(repr(self.pilha), "[3, 2, 1]")

    def test_valores_repetidos_e_none(self):
        self.pilha.push(None)
        self.pilha.push(None)
        self.pilha.push(10)
        self.pilha.push(10)
        self.assertEqual(self.pilha.pop(), 10)
        self.assertEqual(self.pilha.pop(), 10)
        self.assertIsNone(self.pilha.pop())
        self.assertIsNone(self.pilha.pop())


class TestFilaEncadeada(unittest.TestCase):

    def setUp(self):
        self.fila = FilaEncadeada()

    def test_fila_inicial_vazia(self):
        self.assertTrue(self.fila.esta_vazia())
        self.assertEqual(len(self.fila), 0)

    def test_ordem_fifo(self):
        elementos = ["Primeiro", 2, 3.0, None]
        for elem in elementos:
            self.fila.enfileirar(elem)

        for elem in elementos:
            self.assertEqual(self.fila.desenfileirar(), elem)

    def test_excecao_desenfileirar_fila_vazia(self):
        with self.assertRaises(IndexError):
            self.fila.desenfileirar()

    def test_frente_sem_remover(self):
        self.fila.enfileirar("X")
        self.fila.enfileirar("Y")
        self.assertEqual(self.fila.frente(), "X")
        self.assertEqual(len(self.fila), 2) 

    def test_excecao_frente_fila_vazia(self):
        with self.assertRaises(IndexError):
            self.fila.frente()

    def test_intercalacao_operacoes(self):
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        self.assertEqual(self.fila.desenfileirar(), 1) 

        self.fila.enfileirar(3)  
        self.assertEqual(self.fila.frente(), 2)
        self.assertEqual(self.fila.desenfileirar(), 2)  
        self.assertEqual(self.fila.desenfileirar(), 3) 

        self.assertTrue(self.fila.esta_vazia())

    def test_esvaziar_e_reutilizar_instancia(self):
        self.fila.enfileirar("A")
        self.fila.desenfileirar()
        self.assertTrue(self.fila.esta_vazia())


        self.fila.enfileirar("B")
        self.assertFalse(self.fila.esta_vazia())
        self.assertEqual(self.fila.frente(), "B")
        self.assertEqual(self.fila.desenfileirar(), "B")

    def test_coerencia_len(self):
        self.assertEqual(len(self.fila), 0)
        self.fila.enfileirar(10)
        self.assertEqual(len(self.fila), 1)
        self.fila.enfileirar(20)
        self.assertEqual(len(self.fila), 2)

        self.fila.desenfileirar()
        self.assertEqual(len(self.fila), 1)

        self.fila.enfileirar(30)
        self.assertEqual(len(self.fila), 2)

    def test_representacao_repr(self):
        self.fila.enfileirar("frente")
        self.fila.enfileirar("meio")
        self.fila.enfileirar("fim")
        # Deve exibir da frente para o fim
        self.assertEqual(repr(self.fila), "[frente, meio, fim]")

    def test_ausencia_de_acesso_privado(self):
        """Valida que FilaEncadeada utiliza PilhaEncadeada por composição sem expor/acessar atributos privados."""
        self.assertTrue(hasattr(self.fila, "pilha_entrada"))
        self.assertTrue(hasattr(self.fila, "pilha_saida"))
        self.assertIsInstance(self.fila.pilha_entrada, PilhaEncadeada)
        self.assertIsInstance(self.fila.pilha_saida, PilhaEncadeada)


if __name__ == "__main__":
    unittest.main()