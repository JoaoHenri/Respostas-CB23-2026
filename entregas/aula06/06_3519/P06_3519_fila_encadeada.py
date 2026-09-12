import importlib 
pilha_encadeada = importlib.import_module('P06_3519_pilha_encadeada')

Node = pilha_encadeada.Node
PilhaEncadeada = pilha_encadeada.PilhaEncadeada

class Fila_Encadeada:
    def __init__(self):
        self.pilha_de_adicao = PilhaEncadeada()
        self.pilha_de_retirada = PilhaEncadeada()

    def enfileirar(self,item):
        """Adiciona um elemento no fim da fila.
        Complexidade: O(1)"""
        self.pilha_de_adicao.push(item)

    def desenfileirar(self):
        """Retira o primeiro elemento da fila.
        Complexidade: O(1) amortizada (caso médio)"""
        if self.pilha_de_retirada.esta_vazia():
            if not self.pilha_de_adicao.esta_vazia():
                while not self.pilha_de_adicao.esta_vazia():
                    elemento = self.pilha_de_adicao.pop()
                    self.pilha_de_retirada.push(elemento)
                    
            else:
                raise IndexError('Não é possível retirar elementos da fila, pois ela está vazia!')

        return self.pilha_de_retirada.pop()

    def frente(self):
        """Retorna o primeiro elemento da fila.
        Complexidade: O(1) amortizada"""
        if self.pilha_de_retirada.esta_vazia():
            if not self.pilha_de_adicao.esta_vazia():            
                while not self.pilha_de_adicao.esta_vazia():
                    elemento = self.pilha_de_adicao.pop()
                    self.pilha_de_retirada.push(elemento)
                            
            else:
                    raise IndexError('Não é possível selecionar o primeiro elemento da fila, pois ela está vazia!')
        return self.pilha_de_retirada.topo()

    def esta_vazia(self):
        """Verifica se a fila está vazia.
        Complexidade: O(1)"""
        return (len(self.pilha_de_retirada) + len(self.pilha_de_adicao) == 0)

    def __len__(self):
        """Retorna o tamanho da fila.
        Complexidade: O(1)"""
        return (len(self.pilha_de_retirada) + len(self.pilha_de_adicao))

    def __repr__(self):
        """Apresenta a representação textual da fila.
        Complexidade: O(N)"""    
        if not self.pilha_de_retirada.esta_vazia():
            texto_retirada = str(self.pilha_de_retirada)

            if not self.pilha_de_adicao.esta_vazia():
                pilha_reserva = PilhaEncadeada()
                for _ in range(len(self.pilha_de_adicao)):
                    elemento = self.pilha_de_adicao.pop()
                    pilha_reserva.push(elemento)
                texto_reserva = str(pilha_reserva)    
                

                for __ in range(len(pilha_reserva)):
                    elemento = pilha_reserva.pop()
                    self.pilha_de_adicao.push(elemento)

                return(texto_retirada + ' --> '+ texto_reserva)

            else:
                return(texto_retirada)

        elif not self.pilha_de_adicao.esta_vazia():
            while not self.pilha_de_adicao.esta_vazia():
                elemento = self.pilha_de_adicao.pop()
                self.pilha_de_retirada.push(elemento)

            texto = str(self.pilha_de_retirada)

            while not self.pilha_de_retirada.esta_vazia():
                    elemento = self.pilha_de_retirada.pop()
                    self.pilha_de_adicao.push(elemento)

            return(texto)

        else:
            return ''


