'''
2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа
должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать
скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот
код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
'''

import random

simple_list = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,	61,	67,	71, 73,	79,	83,
    89, 97,	101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,	163, 167, 173, 179,
    181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
    281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
    397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
    503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 
    619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
    743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
    863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
    997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069
    ]

def test(func):
    for _ in range(20):
        i = random.randint(0, len(simple_list) - 1)
        if func(i + 1) == simple_list[i]:
            print(f'ОК. {i + 1} простое число равно {simple_list[i]}')
        else:
            print(f'FAIL. {i + 1} простое число не равно {simple_list[i]}')

def simple_eratosthenes(n):
    num_list = [i for i in range(n * 10)]
    num_list[1] = 0
    counter = 0
    for i in range(2, len(num_list)-1):
        if num_list[i] != 0:
            j = i * 2
            while j < len(num_list):
                num_list[j] = 0
                j += i
            counter += 1
        else:
            continue
        if counter == n:
            return num_list[i]

# test(simple_eratosthenes)

# lesson4_task2.simple_eratosthenes(2)
# 1000 loops, best of 5: 6.49 usec per loop

# lesson4_task2.simple_eratosthenes(20)
# 1000 loops, best of 5: 47 usec per loop

# lesson4_task2.simple_eratosthenes(75)
# 1000 loops, best of 5: 241 usec per loop

# lesson4_task2.simple_eratosthenes(100)
# 1000 loops, best of 5: 330 usec per loop

# lesson4_task2.simple_eratosthenes(200)
# 1000 loops, best of 5: 723 usec per loop

# lesson4_task2.simple_eratosthenes(500)
# 100 loops, best of 5: 1.93 msec per loop

# lesson4_task2.simple_eratosthenes(1000)
# 100 loops, best of 5: 4.09 msec per loop

def simple_classic(n):
    simples = []
    num = 2
    while len(simples) != n:
        is_simple = True
        for simple in simples:
            if num % simple == 0:
                is_simple = False
                break
        if is_simple:
            simples.append(num)
        num += 1
    return simples[-1]

# test(simple_classic)

# lesson4_task2.simple_classic(2)
# 1000 loops, best of 5: 1.11 usec per loop

# lesson4_task2.simple_classic(20)
# 1000 loops, best of 5: 26.2 usec per loop

# lesson4_task2.simple_classic(75)
# 1000 loops, best of 5: 241 usec per loop

# lesson4_task2.simple_classic(100)
# 1000 loops, best of 5: 429 usec per loop

# lesson4_task2.simple_classic(200)
# 1000 loops, best of 5: 1.65 msec per loop

# lesson4_task2.simple_classic(500)
# 1000 loops, best of 5: 10.1 msec per loop

# lesson4_task2.simple_classic(1000)
# 1000 loops, best of 5: 36.9 msec per loop

'''Скорость работы классического метода нахождения простых чисел до определенного момента (n = 75)
оказывается выше, чем у метода с использованием "решета Эратосфена", но с учеличением n это меняется,
и уже метод с использованием "решета Эратосфена" показывает лучшее время. Анализируя полученные
результаты, можно придти к выводу, что классический метод имеет сложность O(nlog(n)), метод с
использованием "решета Эратосфена" - O(n).'''
