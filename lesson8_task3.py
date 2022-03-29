'''
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором
все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''

import random

def generate_graph(n):
    graph = [set() for _ in range(n)]
    for i, vertex in enumerate(graph):
        if n == 2:
            edge_num = 1
        else:
            edge_num = random.randint(2, n // 2 + 1)
        while len(vertex) < edge_num:
            edge = random.randint(0, n-1)
            if edge != i:
                vertex.add(edge)
        graph[i] = list(vertex)
    return graph

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(f'Добавлена вершина {start}')
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)
    return visited


n = int(input('Введите количество вершин графа: '))
graph = generate_graph(n)
print('Сгенерированный граф:', *graph, sep='\n')
print(f'Введите номер вершины от 0 до {n-1}, с которой будет совершен обход графа в глубину:')
s = int(input())
dfs(graph, s)
