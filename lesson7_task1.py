'''
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными
числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
'''

import random

def double_bubble_sort(arr, reverse=False):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            if reverse:
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                if i != 0 and arr[i] > arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
            else:
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                if i != 0 and arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
        n += 2
    return arr

m = 50
array = [random.randint(-100, 99) for _ in range(m)]
if m < 100:
    print('Исходный массив:', array, sep='\n')
    print('Отсортированный массив:', double_bubble_sort(array, reverse=True), sep='\n')
else:
    print(
        'Отсортированный функцией double_bubble_sort массив и отсортированный втроенной функцией массив равны?',
        double_bubble_sort(array, reverse=True) == sorted(array, reverse=True)
        )
