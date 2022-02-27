'''
5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
'''

num = int(input('Введите номер буквы в алфавите от a до z: '))
string = 'abcdefghijklmnopqrstuvwxyz'
if num > 0 and num < 27:
    print(f'Ваша буква: {string[num-1]}')
else:
    print('Неверно указан номер буквы.')
