import random


def generate_maze(m, n, room=0, wall=1, cheese='.'):
    

    
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]
    
    def dfs(x, y):

        maze[2 * x + 1][2 * y + 1] = room
        pilha = []
        elemento = []
        elemento.append(x)
        elemento.append(y)
        elemento.append(0)
        another_brick = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(another_brick)
        elemento.append('reserva')
        elemento[-1] = another_brick
        pilha.append(elemento)

        while len(pilha) != 0:
            

            atual = pilha[-1]
            if atual[2] != 4:
                j = atual[2]
                nova_direcao = atual[3][j]
                novo_elemento = []
                novo_elemento.append(atual[0] + nova_direcao[0])
                novo_elemento.append(atual[1] + nova_direcao[1])
                novo_elemento.append(0)
                another_brick = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                random.shuffle(another_brick)
                novo_elemento.append('reserva')
                novo_elemento[-1] = another_brick

                if 0<= novo_elemento[0]< m and 0<= novo_elemento[1] < n and maze[2 * novo_elemento[0] + 1][2 * novo_elemento[1] + 1] == wall:
                    maze[2 * atual[0] + 1 + nova_direcao[0]][2 * atual[1] + 1 + nova_direcao[1]] = room
                    maze[2 * novo_elemento[0] + 1 ][2 * novo_elemento[1] + 1] = room
                    pilha[-1][2] += 1
                    pilha.append(novo_elemento)

                else:
                    pilha[-1][2] += 1
            else:
                pilha.pop()


    dfs(0, 0)
    
    while True:
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * n))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze


def print_maze(maze):

    for row in maze:
        print(" ".join(map(str, row)))


#if __name__ == '__main__':
#    m, n = 15, 17  # Grid size
#    maze = generate_maze(m, n)
#    print('Maze 1')
#    print_maze(maze)

#    room = ' '
#    wall = 'W'
#    cheese = '*'
#    maze = generate_maze(m, n, room, wall, cheese)
#    print('\nMaze 2')
#    print_maze(maze)





room = ' '
wall = '*'
cheese = '.'

def construir_caminho (labirinto,room,cheese, pilha= None, x = 1,y = 1, lista_de_vertices= None):
    def buscador(labirinto,room,cheese, pilha= None, x = 1,y = 1, lista_de_vertices= None):
        if pilha == None:
            pilha = []
        if lista_de_vertices == None:
            lista_de_vertices = []
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        if len(lista_de_vertices) == 0:
            lista_de_vertices.append([x,y])

        lista_de_possibilidades = []
    

        if labirinto[x][y] == cheese:
            lista_de_vertices.append([x,y])
            return lista_de_vertices
        else:
            for i in direcoes:
                nx = x + i[0]
                ny = y + i[1]
                if 0<= nx< len(labirinto) and 0<= ny< len(labirinto[0]) and labirinto[nx][ny] in [cheese, room] and (len(pilha) == 0 or [nx,ny] != pilha[-1]):
                    lista_de_possibilidades.append(i)
            pilha.append([x,y])

            if len(lista_de_possibilidades) == 1:
                nx = x + lista_de_possibilidades[0][0]
                ny = y + lista_de_possibilidades[0][1]
                filho = buscador(labirinto,room, cheese, pilha,nx,ny,lista_de_vertices)
                if filho != 0:
                    lista_de_vertices.append([x,y])
                    return lista_de_vertices
                else:
                    pilha.pop()
                    return 0

            elif len(lista_de_possibilidades) == 0:
                pilha.pop()
                return 0

            else:
                
                for j in lista_de_possibilidades:
                    nx = x + j[0]
                    ny = y + j[1]
                    filho = buscador(labirinto,room, cheese, pilha,nx,ny,lista_de_vertices)
                    if filho != 0:
                        lista_de_vertices.append([x,y])
                        return lista_de_vertices
                pilha.pop()
                return 0

    lista_previa = buscador(labirinto, room, cheese, pilha, x, y, lista_de_vertices)

    def resultado (lista):
        lista_2 = []
        while len(lista) != 0:
            lista_2.append(lista.pop())

        lista_2.pop()
        return (lista_2)

    return resultado(lista_previa)

def visualizador(labirinto_pronto, lista_feita):
    if len(lista_feita) == 1:
        labirinto_pronto[lista_feita[0][0]][lista_feita[0][1]] = 'F'

    else:
        i = 0
        labirinto_pronto[lista_feita[0][0]][lista_feita[0][1]] = 'I'

        i += 1
        while i < len(lista_feita) - 1:
            direcao_tomada = [lista_feita[i][0]-lista_feita[i-1][0],lista_feita[i][1]-lista_feita[i-1][1]]

            if direcao_tomada == [1,0] or direcao_tomada == [-1,0]:
                labirinto_pronto[lista_feita[i][0]][lista_feita[i][1]] = '|'
            else:
                labirinto_pronto[lista_feita[i][0]][lista_feita[i][1]] = '-'
            i += 1
        labirinto_pronto[lista_feita[i][0]][lista_feita[i][1]] = 'F'

    

    return labirinto_pronto


        
                    
labirinto = generate_maze(10, 10, room, wall, cheese)

print_maze(labirinto)
print(construir_caminho(labirinto,room,cheese))
print_maze(visualizador(labirinto,construir_caminho(labirinto,room,cheese)) )