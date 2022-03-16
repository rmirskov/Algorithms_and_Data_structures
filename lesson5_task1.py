'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''

from collections import namedtuple

companies_data = []
New_Company = namedtuple('New_Company', 'name profit_q1 profit_q2 profit_q3 profit_q4')
field_names = [
    'Наименование предприятия: ', 'Прибыль за первый квартал: ',
    'Прибыль за второй квартал: ', 'Прибыль за третий квартал: ','Прибыль за четвертый квартал: '
    ]
profit_sum = 0
while True:
    cur_data = []
    for i in range(len(field_names)):
        if i == 0:
            cur_data.append(input(f'{field_names[i]}'))
        else:
            cur_data.append(float(input(f'{field_names[i]}')))
    profit_sum += sum(cur_data[1:])
    companies_data.append(New_Company(*cur_data))
    off = input('Продолжить ввод? (0 - для выхода, любой символ - для дальнейшего ввода): ')
    if off == '0':
        break

mean_profit = profit_sum / len(companies_data)
print(f'Средняя годовая прибыль равна: {round(mean_profit, 2)}')
great_profit = [c[0] for c in companies_data if sum(c[1:]) > mean_profit]
print('Предприятия с годовой прибылью выше среднего:', *great_profit, sep='\n->')
less_profit = [c[0] for c in companies_data if sum(c[1:]) < mean_profit]
print('Предприятия с годовой прибылью ниже среднего:', *less_profit, sep='\n->')
