'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным
использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде
комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора
Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.
Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой
переменной, а проявили творчество, фантазию и создали универсальный код для замера памяти.
'''

import sys
import random
from collections import Counter

print(sys.version, sys.platform)  # 3.8.10 (default, Nov 26 2021, 20:14:08) [GCC 9.3.0] linux


def count_size(arr):
    result = 0
    for elem in arr:
        if hasattr(elem, '__iter__'):
            if isinstance(elem, dict):
                for k, v in elem.items():
                    result += (sys.getsizeof(k) + sys.getsizeof(v))
            elif not isinstance(elem, str):
                for v in elem:
                    result += sys.getsizeof(v)
        result += sys.getsizeof(elem)
    return result
        
'''3_4. Определить, какое число в массиве встречается чаще всего.'''

def find_most_frequent_number_1(num_list):
    counter_dict = {}

    for num in num_list:
        if num not in counter_dict.keys():
            counter_dict[num] = 1
        else: 
            counter_dict[num] += 1

    max_count = 0
    for num, count in counter_dict.items():
        if count > max_count:
            max_count = count

    max_count_num = [num for num, count in counter_dict.items() if count == max_count]
    if len(max_count_num) == 1:
        print(f'Число {max_count_num[0]} встречается {max_count} раз в исходном массиве.')
    else:
        print(f'Числа', *max_count_num, f'встречаются по {max_count} раз в исходном массиве.')
    print(sys.getsizeof(find_most_frequent_number_1) + count_size([
        num_list, num, counter_dict, max_count, max_count_num, count
        ]))


def find_most_frequent_number_2(num_list):
    max_count = 0
    checked_numbers = []
    max_count_numbers = []

    for num in num_list:
        if num not in checked_numbers:
            checked_numbers.append(num)
            current_count = num_list.count(num)
            if current_count > max_count:
                max_count_numbers = [num]
                max_count = current_count
            elif current_count == max_count:
                max_count_numbers.append(num)

    if len(max_count_numbers) == 1:
        print(f'Число {max_count_numbers[0]} встречается {max_count} раз в исходном массиве.')
    else:
        print(f'Числа', *max_count_numbers, f'встречаются по {max_count} раз в исходном массиве.')
    print(sys.getsizeof(find_most_frequent_number_2) + count_size([
        num_list, num, checked_numbers, max_count, max_count_numbers, current_count
        ]))


def find_most_frequent_number_3(num_list):
    sorted_counter = sorted(Counter(num_list).items(), key=lambda x: x[1], reverse=True)
    max_count = sorted_counter[0][1]
    max_count_numbers = [x[0] for x in sorted_counter if x[1] == max_count]
    
    if len(max_count_numbers) == 1:
        print(f'Число {max_count_numbers[0]} встречается {max_count} раз в исходном массиве.')
    else:
        print(f'Числа', *max_count_numbers, f'встречаются по {max_count} раз в исходном массиве.')
    print(sys.getsizeof(find_most_frequent_number_2) + count_size([
        num_list, sorted_counter, max_count, max_count_numbers
        ]))

size = 10000
lower_bound = 0
upper_bound = 1000
num_list = [random.randint(lower_bound, upper_bound) for _ in range(size)]

find_most_frequent_number_1(num_list)  # 460956
find_most_frequent_number_2(num_list)  # 404992
find_most_frequent_number_3(num_list)  # 433056

size_2 = 10000
lower_bound_2 = 0
upper_bound_2 = 400
num_list_2 = [random.randint(lower_bound_2, upper_bound_2) for _ in range(size_2)]

find_most_frequent_number_1(num_list_2)  # 408800
find_most_frequent_number_2(num_list_2)  # 382324
find_most_frequent_number_3(num_list_2)  # 393940

'''Второй вариант решения занимает меньшее количество памяти из-за того, что в нем для хранения данных
используются списки, а не словари. Разница в занимаемой памяти будет увеличиваться с ростом словаря.'''
