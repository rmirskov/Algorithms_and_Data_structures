'''
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал
список вершин, которые необходимо обойти.
'''

def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False for _ in range(length)]
    cost = [float('inf') for _ in range(length)]
    parent = [-1 for _ in range(length)]
    path = [[] for _ in range(length)]

    cost[start] = 0
    min_cost = 0
    
    while min_cost < float('inf'):
        is_visited[start] = True
        if parent[start] != -1:
            path[start].extend(path[parent[start]])
        path[start].append(start)

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
        
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return zip(range(8), cost, path)

graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
    ]

print(f'В графе количество вершин равно {len(graph)}.')
start = int(input('От какой вершины идти: '))
for i, s, p in dijkstra(graph, start):
    print(f'От вершины {start} до вершины {i} расстояние равно {s}, путь {p}')
