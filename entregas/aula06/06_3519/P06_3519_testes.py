import unittest
import importlib

pilha_encadeada = importlib.import_module('P06_3519_pilha_encadeada')
fila_encadeada = importlib.import_module('P06_3519_fila_encadeada')

Pilha_Encadeada = pilha_encadeada.PilhaEncadeada
Fila_Encadeada = fila_encadeada.Fila_Encadeada

class TestPilhaEncadeada(unittest.TestCase):
    def test_ordem_LIFO(self):
        """Testa se a ordem de saída está seguindo a lógica de stack."""

        exemplar_de_pilha = Pilha_Encadeada()

        exemplar_de_pilha.push('Corinthians maior do mundo!')
        exemplar_de_pilha.push('Korn melhor banda!')
        exemplar_de_pilha.push('F = ma')

        self.assertEqual(exemplar_de_pilha.pop(), 'F = ma')
        self.assertEqual(exemplar_de_pilha.pop(), 'Korn melhor banda!')
        self.assertEqual(exemplar_de_pilha.pop(),'Corinthians maior do mundo!')

    def test_operacao_em_vazio(self):
        pilha_teste = Pilha_Encadeada()

        self.assertTrue(pilha_teste.esta_vazia())

        with self.assertRaises(IndexError):
            pilha_teste.pop()

        with self.assertRaises(IndexError):
            pilha_teste.topo()

    def test_medidor_de_tamanho(self):
        pilha_cobaia = Pilha_Encadeada()

        self.assertEqual(len(pilha_cobaia),0)
        pilha_cobaia.push(2.71)
        self.assertEqual(len(pilha_cobaia),1)
        pilha_cobaia.push(3.141579)
        self.assertEqual(len(pilha_cobaia),2)
        pilha_cobaia.push('Are you ready?')


        self.assertEqual(len(pilha_cobaia),3)

        pilha_cobaia.pop()
        self.assertEqual(len(pilha_cobaia),2)
        pilha_cobaia.pop()
        self.assertEqual(len(pilha_cobaia),1)
        pilha_cobaia.pop()
        self.assertEqual(len(pilha_cobaia),0)

    def test_variacao_insercao_remocao(self):
        mais_uma_pilha = Pilha_Encadeada()

        mais_uma_pilha.push('Olá')
        self.assertEqual(mais_uma_pilha.topo(),'Olá')

        mais_uma_pilha.push(100)
        mais_uma_pilha.push(0.0000001)
        self.assertEqual(mais_uma_pilha.topo(), 0.0000001)

        mais_uma_pilha.pop()
        self.assertEqual(mais_uma_pilha.topo(),100)

        mais_uma_pilha.pop()
        self.assertEqual(mais_uma_pilha.topo(),'Olá')

        mais_uma_pilha.push('PS2 > PS5')
        self.assertEqual(mais_uma_pilha.topo(),'PS2 > PS5')

        mais_uma_pilha.push(14)
        self.assertEqual(mais_uma_pilha.topo(), 14)

        mais_uma_pilha.pop()
        mais_uma_pilha.pop()
        mais_uma_pilha.pop()
        self.assertTrue(mais_uma_pilha.esta_vazia())


    def test_de_tipos_e_None(self):
        nova_pilha = Pilha_Encadeada()
        elementos = ['war', 'attack', 'prison song', 67, 13, 22, 14, None ]
        for coisa in elementos:
            nova_pilha.push(coisa)
            self.assertEqual(nova_pilha.topo(),coisa)

        self.assertEqual(len(nova_pilha), len(elementos))

        for outra_coisa in (reversed(elementos)):
            fato = nova_pilha.pop()
            self.assertEqual(fato, outra_coisa)

        self.assertEqual(len(nova_pilha), 0)




class TestFilaEncadeada(unittest.TestCase):
    def test_ordem_FIFO(self):
        """Testa se a ordem de saída está seguindo a lógica de fila."""

        exemplar_de_fila = Fila_Encadeada()

        exemplar_de_fila.enfileirar('Corinthians maior do mundo!')
        exemplar_de_fila.enfileirar('Korn melhor banda!')
        exemplar_de_fila.enfileirar('F = ma')

        self.assertEqual(exemplar_de_fila.desenfileirar(), 'Corinthians maior do mundo!')
        self.assertEqual(exemplar_de_fila.desenfileirar(), 'Korn melhor banda!')
        self.assertEqual(exemplar_de_fila.desenfileirar(),'F = ma')

    def test_operacao_em_vazio(self):
        fila_teste = Fila_Encadeada()

        self.assertTrue(fila_teste.esta_vazia())

        with self.assertRaises(IndexError):
            fila_teste.desenfileirar()

        with self.assertRaises(IndexError):
            fila_teste.frente()

    def test_medidor_de_tamanho(self):
        fila_cobaia = Fila_Encadeada()

        self.assertEqual(len(fila_cobaia),0)
        fila_cobaia.enfileirar(2.71)
        self.assertEqual(len(fila_cobaia),1)
        fila_cobaia.enfileirar(3.141579)
        self.assertEqual(len(fila_cobaia),2)
        fila_cobaia.enfileirar('Are you ready?')


        self.assertEqual(len(fila_cobaia),3)

        fila_cobaia.desenfileirar()
        self.assertEqual(len(fila_cobaia),2)
        fila_cobaia.desenfileirar()
        self.assertEqual(len(fila_cobaia),1)
        fila_cobaia.desenfileirar()
        self.assertEqual(len(fila_cobaia),0)

    def test_variacao_insercao_remocao(self):
        mais_uma_fila = Fila_Encadeada()

        mais_uma_fila.enfileirar('Olá')
        self.assertEqual(mais_uma_fila.frente(),'Olá')

        mais_uma_fila.enfileirar(100)
        mais_uma_fila.enfileirar(0.0000001)
        self.assertEqual(mais_uma_fila.frente(), 'Olá')

        mais_uma_fila.desenfileirar()
        self.assertEqual(mais_uma_fila.frente(),'Olá')

        mais_uma_fila.desenfileirar()
        self.assertEqual(mais_uma_fila.frente(),'Olá')

        mais_uma_fila.enfileirar('PS2 > PS5')
        self.assertEqual(mais_uma_fila.frente(),'Olá')

        mais_uma_fila.enfileirar(14)
        self.assertEqual(mais_uma_fila.frente(), 'Olá')

        mais_uma_fila.desenfileirar()
        mais_uma_fila.desenfileirar()
        mais_uma_fila.desenfileirar()
        self.assertTrue(mais_uma_fila.esta_vazia())


    def test_de_tipos_e_None(self):
        nova_fila = Fila_Encadeada()
        elementos = ['war', 'attack', 'prison song', 67, 13, 22, 14, None ]
        for coisa in elementos:
            nova_fila.enfileirar(coisa)
            self.assertEqual(nova_fila.frente(),'war')

        self.assertEqual(len(nova_fila), len(elementos))

        for coisita in (elementos):
            fato = nova_fila.desenfileirar()
            self.assertEqual(fato, coisita)

        self.assertEqual(len(nova_fila), 0)