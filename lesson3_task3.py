'''3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

import random

size = 20
lower_bound = 0
upper_bound = size * 5
num_list = [random.randint(lower_bound, upper_bound) for _ in range(size)]
num_list = list(set(num_list))  # исключим повторяющиеся значения, чтобы однозначно определить max и min
print('Исходный массив: ')
print(num_list)
min_num, max_num = upper_bound, lower_bound
min_ind, max_ind = -1, -1
for i, num in enumerate(num_list):
    if num > max_num:
        max_num = num
        max_ind = i
    if num < min_num:
        min_num = num
        min_ind = i
num_list[min_ind], num_list[max_ind] = num_list[max_ind], num_list[min_ind]
print('Измененный массив: ')
print(num_list)
