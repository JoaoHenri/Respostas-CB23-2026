class Node:
    def __init__(self, dado, proximo = None):
        self.dado = dado
        self.proximo = proximo

class PilhaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def push(self, algo):
        """Adiciona o elemento escolhido ao topo da pilha.
        Complexidade: O(1)"""
        a_inserir = Node(algo, self.cabeca)
        self.cabeca = a_inserir
        self.tamanho += 1

    def pop(self):
        """Remove o elemento do topo da pilha caso esta não esteja vazia.
        Complexidade: O(1)"""
        if self.tamanho == 0:
            raise IndexError('Não é possível remover elementos, pois a pilha está vazia!')
        elemento = self.cabeca
        self.cabeca = self.cabeca.proximo
        self.tamanho -= 1
        return elemento.dado


    def topo(self):
        """Consulta o elemento no topo da pilha caso esta não esteja vazia.
        Complexidade: O(1)"""
        if self.tamanho == 0:
            raise IndexError('Não é possível consultar seu topo, pois a pilha está vazia!')
        resposta = self.cabeca
        return resposta.dado

    def esta_vazia(self):
        """Verifica se a pilha está vazia.
        Complexidade: O(1)"""
        return self.tamanho == 0

    def __len__(self):
        """Retorna o tamanho da pilha.
        Complexidade: O(1)"""
        return self.tamanho

    def __repr__(self):
        """Retorna a representação textual da pilha.
         Complexidade: O(N) """
        if self.tamanho != 0:
            item = self.cabeca
            texto = ''
            while item.proximo != None:
                texto = texto + f'{item.dado}' + ' --> '
                item = item.proximo
            texto = texto + f'{item.dado}'
            return texto
        else:
            return ''
    
