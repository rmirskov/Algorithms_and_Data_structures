'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в
массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
'''

import random

size = 200
lower_bound = - size * 2
upper_bound = size * 2
num_list = list(set([random.randint(lower_bound, upper_bound) for _ in range(size)]))

max_negative_num = lower_bound
max_negative_ind = -1

for i, num in enumerate(num_list):
    if num < 0 and num > max_negative_num:
        max_negative_num = num
        max_negative_ind = i

print(f'Максимальный отрицательный элемент равен {max_negative_num}',
     f'и занимает {max_negative_ind} позицию в массиве .')
