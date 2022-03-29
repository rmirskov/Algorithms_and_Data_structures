'''
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''
from itertools import permutations

n = int(input('Введите количество друзей: '))

def friends_graph(n):
    friends = [i for i in range(n)]
    return permutations(friends, 2)

print('Граф, состоящий из списка ребер:', *friends_graph(n), sep='\n')

def handshakes_counter(graph):
    counter_list = []
    for x in graph:
        if set(x) not in counter_list:
            counter_list.append(set(x))
    return len(counter_list)

print(f'Количество уникальных рукопожатий равно {handshakes_counter(friends_graph(n))}')