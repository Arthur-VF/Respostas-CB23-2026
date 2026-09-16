# python 3

"""
maze_builder.py
---------------
Geração procedural de labirintos perfeitos usando busca em profundidade (DFS)
com retrocesso (backtracking).

Um labirinto "perfeito" possui exactamente um caminho entre quaisquer dois
pontos — equivalente a uma árvore geradora aleatória sobre a grade m x n.

Representação interna
~~~~~~~~~~~~~~~~~~~~~
A grade lógica de m linhas X n colunas é expandida para uma matriz de
(2m+1) X (2n+1) células, onde:
  - células de coordenadas ímpares (2i+1, 2j+1) representam salas (rooms);
  - células entre duas salas adjacentes representam paredes derrubáveis;
  - as bordas externas são sempre paredes.

O queijo (cheese) é colocado aleatoriamente em qualquer sala.
"""

import random


def generate_maze(m, n, room=0, wall=1, cheese='.'):
    """Gera um labirinto perfeito de m X n células usando DFS com backtracking.

    Parameters
    ----------
    m : int
        Número de linhas da grade lógica.
    n : int
        Número de colunas da grade lógica.
    room : int or str, optional
        Valor usado para representar passagens abertas. Padrão: 0.
    wall : int or str, optional
        Valor usado para representar paredes. Padrão: 1.
    cheese : str, optional
        Símbolo colocado aleatoriamente em uma sala como objetivo. Padrão: '.'.

    Returns
    -------
    list[list]
        Matriz (2m+1) X (2n+1) representando o labirinto gerado.
    """
    # Inicializa a matriz expandida com todas as células como parede
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    # Deslocamentos para os quatro vizinhos cardeais: N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

   
    def dfs_iterativo(x, y):
        maze[2 * x + 1][2 * y + 1] = room

        posicao_atual = [(x, y)]
        visitados = [(x, y)]

        while True:
            if posicao_atual == []:
                break

            x = posicao_atual[-1][0]
            y = posicao_atual[-1][1]

            entrou = False

            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visitados:
                    maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
                    maze[2 * nx + 1][2 * ny + 1] = room

                    posicao_atual.append((nx, ny))
                    visitados.append((nx, ny))

                    entrou = True
                    break

            if entrou == False:
                posicao_atual.pop(-1)

    # Inicia a DFS no canto superior-esquerdo da grade lógica
    dfs_iterativo(0, 0)

    # Posiciona o queijo em uma sala aleatória (rejeita paredes)
    while True:
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * m))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze


def encontrar_caminho(maze):
    x = 1
    y = 1
    posicao_atual = [(x,y)]
    visitados = [(x,y)]

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == cheese:
                final = (i,j)

    while True:

        if posicao_atual[-1] == final:
            posicao_atual.pop(-1)
            for i in range(len(posicao_atual)):
                maze[posicao_atual[i][0]][posicao_atual[i][1]] = '.'
            break

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)

        entrou = False

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and (nx, ny) not in visitados and maze[nx][ny] != wall:
                posicao_atual.append((nx,ny))
                visitados.append((nx,ny))
                entrou = True
                x = nx
                y = ny
                break

        if entrou == False:
            posicao_atual.pop(-1)
            if posicao_atual != []:
                x = posicao_atual[-1][0]
                y = posicao_atual[-1][1]
            else:
                return("impossível")

    



def print_maze(maze):
    """Imprime o labirinto no terminal, uma linha por vez.

    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    for row in maze:
        print(" ".join(map(str, row)))

# Example usage:
if __name__ == '__main__':
    m, n = 10, 14 # Grid size
    random.seed(11110)
    maze = generate_maze(m, n)
    print('Maze 1')
    print_maze(maze)

    room = ' '
    wall = 'W'
    cheese = '*'
    maze = generate_maze(m, n, room, wall, cheese)
    encontrar_caminho(maze)
    print('\nMaze 2')
    print_maze(maze)


