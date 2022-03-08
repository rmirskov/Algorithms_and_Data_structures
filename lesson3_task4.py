'''4. Определить, какое число в массиве встречается чаще всего.'''

import random

size = 1000
lower_bound = 0
upper_bound = 200
num_list = [random.randint(lower_bound, upper_bound) for _ in range(size)]
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

