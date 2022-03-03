'''
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число
34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

num = int(input('Введите натуральное число: '))
even_digits = 0
odd_digits = 0
while num > 0:
    current_digit = num % 10
    if current_digit % 2 == 0:
        even_digits += 1
    else:
        odd_digits += 1
    num = num // 10
print(f'Во введенном числе четных чисел - {even_digits}, нечетных чисел - {odd_digits}.')
