'''
3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
'''

import random

print(
    'Выберите режим генерации:',
    'a - случайное целое число,',
    'b - случайное вещественное число,',
    'c - случайный символ от a до z.', sep='\n'
    )

mode = input('>>>').lower()

if mode == 'a':
    print('Введите диапазон для случайного целого числа через пробел: ')
    z1, z2 = (int(elem) for elem in input('>>>').split(' '))
    if z1 < z2:
        z = random.randint(z1, z2)
    else:
        z = random.randint(z2, z1)
    print(f'Ваше случайное целое число: {z}')
elif mode == 'b':
    print('Введите диапазон для случайного вещественного числа через пробел: ')
    r1, r2 = (float(elem) for elem in input('>>>').split(' '))
    if r1 < r2:
        r = random.uniform(r1, r2)
    else:
        r = random.uniform(r2, r1)
    print(f'Ваше случайное вещественное число: {r}')
elif mode == 'c':
    string = 'abcdefghijklmnopqrstuvwxyz'
    print('Введите диапазон для случайного символа от a до z через пробел: ')
    s1, s2 = (string.find(elem) for elem in input('>>>').split(' '))
    if s1 < s2:
        s = string[random.randint(s1, s2)]
    else:
        s = string[random.randint(s2, s1)]
    print(f'Ваш случайный символ от a до z: {s}')
else:
    print('Неверный выбран режим генерации.')