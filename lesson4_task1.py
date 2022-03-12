'''4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n)
вводится с клавиатуры.
'''

series_sum = [1.0, 0.5, 0.75, 0.625, 0.6875, 0.65625, 0.671875, 0.6640625]

def test(func):
    for i in range(len(series_sum)):
        if func(i + 1) == series_sum[i]:
            print(f'ОК. Сумма ряда из {i + 1} элементов равна {series_sum[i]}')
        else:
            print(f'FAIL. Сумма ряда из {i + 1} элементов не равна {series_sum[i]}')

def get_series_sum_1(n):
    '''Используем цикл'''
    result = 0
    i = 1
    while i <= n:
        result += 1 / (-2)**(i - 1)
        i += 1
    return result

# test(get_series_sum_1)

# lesson4_task1.get_series_sum_1(5)
# 1000 loops, best of 5: 1.84 usec per loop

# lesson4_task1.get_series_sum_1(50)
# 1000 loops, best of 5: 20.5 usec per loop

# lesson4_task1.get_series_sum_1(100)
# 1000 loops, best of 5: 54.7 usec per loop

# lesson4_task1.get_series_sum_1(200)
# 1000 loops, best of 5: 135 usec per loop

# lesson4_task1.get_series_sum_1(400)
# 1000 loops, best of 5: 331 usec per loop

# lesson4_task1.get_series_sum_1(800)
# 1000 loops, best of 5: 851 usec per loop

# lesson4_task1.get_series_sum_1(8000)
# 1000 loops, best of 5: 51.7 msec per loop

def get_series_sum_2(n):
    '''Используем рекурсию'''
    if n == 0:
        return 0
    else:
        return  1 / (-2)**(n - 1) + get_series_sum_2(n-1)

# test(get_series_sum_2)

# lesson4_task1.get_series_sum_2(5)
# 1000 loops, best of 5: 2.1 usec per loop

# lesson4_task1.get_series_sum_2(50)
# 1000 loops, best of 5: 23.6 usec per loop

# lesson4_task1.get_series_sum_2(100)
# 1000 loops, best of 5: 62.1 usec per loop

# lesson4_task1.get_series_sum_2(200)
# 1000 loops, best of 5: 152 usec per loop

# lesson4_task1.get_series_sum_2(400)
# 1000 loops, best of 5: 377 usec per loop

# lesson4_task1.get_series_sum_2(800)
# 1000 loops, best of 5: 937 usec per loop

def get_series_sum_3(n):
    '''Используем формулу для нахождения суммы n членов геометрической прогрессии'''
    b1 = 1
    q = -1/2
    return b1 * (q**n - 1) / (q - 1)

# test(get_series_sum_3)

# lesson4_task1.get_series_sum_3(5)
# 1000 loops, best of 5: 616 nsec per loop

# lesson4_task1.get_series_sum_3(50)
# 1000 loops, best of 5: 699 nsec per loop

# lesson4_task1.get_series_sum_3(100)
# 1000 loops, best of 5: 582 nsec per loop

# lesson4_task1.get_series_sum_3(200)
# 1000 loops, best of 5: 374 nsec per loop

# lesson4_task1.get_series_sum_3(400)
# 1000 loops, best of 5: 615 nsec per loop

# lesson4_task1.get_series_sum_3(800)
# 1000 loops, best of 5: 380 nsec per loop

# lesson4_task1.get_series_sum_3(8000)
# 1000 loops, best of 5: 624 nsec per loop

'''Как можно видеть, наилучший результат дает третий вариант со сложностью O(1), который не зависит
от параметра n. Два остальных варианта дают схожие по скорости работы результаты, только вариант через
рекурсию ограничен глубиной рекурсии. Сложность первого и второго вариантов похожа на O(nlog(n))'''

