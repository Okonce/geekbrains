# import timeit
import cProfile
import functools

# x = 2 + 2
# print(timeit.timeit('x = 2 + 2'))
# print(timeit.timeit('x = sum(range(10))'))

# Либо можно через консоль, что более интересно
#  python -m timeit -n 100 -s "import main"
# 100 loops, best of 5: 4.58 nsec per loop
# usec - микро сек 10-6
# msec - 10-3

# ----------------------------------------------------------------------------------------------------------------------
# def get_let(data):
#     return len(data)
#
# def get_sum(data):
#     s = 0
#     for x in data:
#         s += x
#     return s
#
# def get_main():
#     ls = [x for x in range(100_000_000)]
#     a = get_let(ls)
#     b = get_sum(ls)
#
# cProfile.run('get_main()') -> будет ввиде таблицы, сколько что вызывалось сколько раз и какое время потрачено
# ----------------------------------------------------------------------------------------------------------------------

# Оптимизация кода с помощью алгоритма поиска Чисел Фибоначи
def test_fib(func): # тестировщик кода
    fst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for num, i in enumerate(fst):
        assert i == func(num)
        print(f'Test {num} OK')

@functools.lru_cache() # декоратор запоминает какие n были и какие числа им соответствуют типо работают как дикт и лист внизу
# данный декоратор дает прирост в работе функции но не избавляет от переполненности стэка вызова функции
def fib(n):  # первый вариант
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def fib_dict(n): # через словарь второй вариант
    fib_d = {0:0, 1:1,}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n-1) + _fib_dict(n-2)
        return fib_d[n]
    return _fib_dict(n)

def fib_list(n): # через список третий вариант
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]
    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n-1) + _fib_list(n-2)
            return fib_l[n]
    return _fib_list(n)

def fib_loop(n): # не через рекурсию четверный вариант
    if n < 2:
        return n
    first, second = 0, 1
    for i in range(2, n+1):
        first, second = second, first + second
    return second

# test_fib(fib_dict)
# test_fib(fib)

# cProfile.run('fib(10)')

# ❯ python -m timeit -n 1000 -s "import main" "main.fib(10)"
# 1000 loops, best of 5: 11.1 usec per loop

# ❯ python -m timeit -n 1000 -s "import main" "main.fib(15)"
# 1000 loops, best of 5: 120 usec per loop

# ❯ python -m timeit -n 1000 -s "import main" "main.fib(20)"
# 1000 loops, best of 5: 1.33 msec per loop

# Как результат надо тестировать допустим 10 15 20 -> первый случай долго это делает. Зависимость O(n2)
# Второй и третий варианты одинаковы по времени O(n), но на самом деле списки весят меньше чем словари
# у рекурсии есть стек ошибки функции

def sieve(number):
    # number = 100
    sieve = [x for x in range(number)]
    sieve[1] = 0

    for x in range(2, number):
        if sieve[x] != 0:
            j = x * 2
            while j < number:
                sieve[j] = 0
                j += x

    results = [x for x in sieve if x != 0]
    return results

# cProfile.run('sieve(10)')

def prime(number):
    # number = 100
    results = [2]
    for x in range(3, number, 2):
        if x > 10 and x % 10 == 5:
            continue
        for j in results:
            if j*j-1 > x:
                results.append(x)
                break
            if x % j == 0:
                break
        else:
            results.append(x)
    return results

import random
import numpy as np

size = 20
matrix = [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]


def first_function():
    list_min = []
    for n, line in enumerate(matrix):
        if n == 0:
            list_min = line
        else:
            for k, (x, y) in enumerate(zip(line, list_min)):
                if x < y:
                    list_min[k] = x

    max_value = 0
    for x in list_min:
        if x > max_value:
            max_value = x
    return max_value

def second_function():
    matrix_array = np.array(matrix)
    return max([min(matrix_array[:, i]) for i in range(size)])

def third_function():
    max_value = 0
    for j in range(5):
        min_value = matrix[0][j]
        for i in range(5):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
        if min_value > max_value:
            max_value = min_value
    return max_value