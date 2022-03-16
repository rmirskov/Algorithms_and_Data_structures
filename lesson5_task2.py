'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как ["A", "2"] и ["C", "4", "F"]
соответственно. Сумма чисел из примера: ["C", "F", "1"], произведение - ["7", "C", "9", "F", "E"].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной
задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
'''

from collections import deque

dex_16 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
hex_16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

dex_hex = {k: v for k, v in zip(dex_16, hex_16)}
hex_dex = {k: v for k, v in zip(hex_16, dex_16)}

def hex_sum(h1, h2):
    if len(h1) > len(h2):
        h2 = '0' * (len(h1) - len(h2)) + h2
    else:
        h1 = '0' * (len(h2) - len(h1)) + h1
    deq_1, deq_2 = deque(h1), deque(h2)
    result = deque()
    add_unit = 0
    while len(deq_1) != 0:
        current_dex_sum = hex_dex[deq_1.pop()] + hex_dex[deq_2.pop()] + add_unit
        first_sign = current_dex_sum // 16
        add_unit = first_sign if first_sign > 0 else 0
        second_sign = current_dex_sum % 16
        result.appendleft(dex_hex[second_sign])
    if add_unit > 0:
        result.appendleft(dex_hex[add_unit])
    return ''.join(result)

def hex_mult(h1, h2):
    deq_1 = deque(h1)
    deq_2 = deque(h2)
    result = '0'
    counter = 0
    while len(deq_2) != 0:
        current_mult = deque()
        add_unit = 0
        m = hex_dex[deq_2.pop()]
        deq_1_copy = deq_1.copy()
        while len(deq_1_copy) != 0:
            current_dex_mult = hex_dex[deq_1_copy.pop()] * m + add_unit
            first_sign = current_dex_mult // 16
            add_unit = first_sign if first_sign > 0 else 0
            second_sign = current_dex_mult % 16
            current_mult.appendleft(dex_hex[second_sign])
        if add_unit > 0:
            current_mult.appendleft(dex_hex[add_unit])
        result = hex_sum(result, ''.join(current_mult) + '0' * counter)
        counter += 1
    return result

def hex_test(arr):
    for elem in arr:
        if hex_sum(elem[0], elem[1]) == elem[2] and hex_mult(elem[0], elem[1]) == elem[3]:
            print('Test OK')
        else:
            print('Test FAIL')

test_list = [
    ('AAA', 'BBB', '1665', '7D182E'),
    ('A2', 'C4F', 'CF1', '7C9FE'),
    ('DA2E', 'B43', 'E571', '999140A'),
    ('57E', '2F6', '874', '104314'),
    ('FF3', 'ABC', '1AAF', 'AB3474'),
    ('123', 'DEF0', 'E013', 'FD6AD0')
]

hex_test(test_list)
