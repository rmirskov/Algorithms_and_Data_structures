'''
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в
диапазоне от 2 до 9. Примечание: 8 разных ответов.
'''

num_list = [i for i in range(2, 100)]

for div in range(2, 10):
    cur_arr = [i for i in num_list if i % div == 0]
    print(f'В диапазоне от 2 до 99 количество чисел кратных числу {div} равно {len(cur_arr)}')
