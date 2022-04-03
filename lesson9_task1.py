'''
1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции
дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib
задача считается не решённой.
'''

from hashlib import sha1
from itertools import combinations

def count_substrings(s):
    hashes = set()
    slices = list(combinations(range(len(s) + 1), 2))
    for slice in slices:
        substr = (s[slice[0]:slice[1]])
        current_hash = sha1(substr.encode('utf-8')).hexdigest()
        if current_hash != sha1(s.encode('utf-8')).hexdigest():
            hashes.add(current_hash)
    return len(hashes)

input_str = input('Введите строку для подсчета подстрок: ')
print(f'Количество подстрок в строке {input_str} равно {count_substrings(input_str)}.')
