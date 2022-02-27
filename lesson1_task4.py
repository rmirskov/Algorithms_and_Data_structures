'''
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв.
'''

let1, let2 = (input('Введите две буквы из диапазона от a до z через пробел: ').split(' '))
string = 'abcdefghijklmnopqrstuvwxyz'
ind1 = string.find(let1)
ind2 = string.find(let2)
if ind1 == ind2:
    print(f'Вы указали одну и ту же букву {let1}. Она находится на {ind1+1} месте в алфавите.')
else:
    if ind1 < ind2:
        let_between = ind2 - ind1 - 1
    else:
        let_between = ind1 - ind2 - 1
    print(
        f'Буква {let1} на {ind1+1} месте в алфавите.',
        f'Буква {let2} на {ind2+1} месте в алфавите.',
        f'Между буквами {let1} и {let2} в алфавите {let_between} букв.', sep='\n'
        )
