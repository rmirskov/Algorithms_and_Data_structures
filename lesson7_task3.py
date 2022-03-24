'''
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве
медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся
элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также
недопустима).
'''

import random

def get_median(array):
    lower_bound = min(array)
    upper_bound = max(array)
    for i in range(len(array)):
        if lower_bound <= array[i] <= upper_bound:
            less_counter2, equal_counter2, more_counter2 = 0, 0, 0
            for elem in array[:i] + array[i+1:]:
                if elem < array[i]:
                    less_counter2 += 1
                elif elem > array[i]:
                    more_counter2 += 1
                else:
                    equal_counter2 += 1
            if abs(less_counter2 - more_counter2) <= equal_counter2:
                return array[i]
            elif more_counter2 - less_counter2 > equal_counter2:
                lower_bound = array[i]
            elif less_counter2 - more_counter2 > equal_counter2:
                upper_bound = array[i]
    return 'Медиану найти не удалось :('

def check_median(array):
    array.sort()
    return array[len(array)//2]

m = 500000
array = [random.randint(-10000, 100000) for _ in range(2 * m + 1)]

print(
    f'Медиана, посчитанная без использования сортировки, равна {get_median(array)}',
    f'Медиана, посчитанная с использованием сортировки, равна {check_median(array)}', sep='\n'
    )
