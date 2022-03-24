'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''

import random

def merge_sort(arr, left, right):
    if right - left > 1:
        mid = (left + right)//2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge_list(arr, left, mid, right)
 
def merge_list(arr, left_pos, mid_pos, right_pos):
    left_arr = arr[left_pos:mid_pos]
    right_arr = arr[mid_pos:right_pos]
    k = left_pos
    i, j = 0, 0
    while (left_pos + i < mid_pos and mid_pos + j < right_pos):
        if (left_arr[i] <= right_arr[j]):
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    if left_pos + i < mid_pos:
        while k < right_pos:
            arr[k] = left_arr[i]
            i += 1
            k += 1
    else:
        while k < right_pos:
            arr[k] = right_arr[j]
            j += 1
            k += 1

m = 100000
array = [random.randint(0, 49) for _ in range(m)]
array_copy = array.copy()

print(
    'Исходный массив и отсортированный втроенной функцией массив равны?',
    array == sorted(array_copy)
    )
if m < 100:
    print(array)

merge_sort(array, 0, len(array))

print(
    'Отсортированный функцией merge_sort массив и отсортированный втроенной функцией массив равны?',
    array == sorted(array_copy)
    )
if m < 100:
    print(array)
