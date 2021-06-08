'''
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
'''

'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

import random
import numpy as np
import cProfile
import sys

print(sys.version, sys.platform)
# 3.8.2 (default, Dec 21 2020, 15:06:03) [Clang 12.0.0 (clang-1200.0.32.29)] darwin

def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__} size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items:
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)

def first_function(matrix):
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

    print(show_size(list_min))
    print(show_size(max_value))

    return max_value

def second_function(matrix):
    matrix_array = np.array(matrix)
    max_value =  max([min(matrix_array[:, i]) for i in range(size)])

    print(show_size(matrix_array))
    print(show_size(max_value))

    return max_value

def third_function(matrix):
    max_value = 0
    for j in range(5):
        min_value = matrix[0][j]
        for i in range(5):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
        if min_value > max_value:
            max_value = min_value

    print(show_size(max_value))

    return max_value

size = 5
matrix = [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]

print(show_size(size)) # type = <class 'int'> size = 28, object = 5
print(show_size(matrix)) # Так как это везде одинаково, то считаем здесь - size 120
'''
type = <class 'list'> size = 120, object = [[72, 99, 54, 10, 48], [64, 13, 30, 90, 27], [67, 89, 55, 24, 65], [76, 39, 91, 38, 42], [41, 51, 59, 14, 86]]
	 type = <class 'list'> size = 120, object = [72, 99, 54, 10, 48]
		 type = <class 'int'> size = 28, object = 72
		 type = <class 'int'> size = 28, object = 99
		 type = <class 'int'> size = 28, object = 54
		 type = <class 'int'> size = 28, object = 10
		 type = <class 'int'> size = 28, object = 48
	 type = <class 'list'> size = 120, object = [64, 13, 30, 90, 27]
		 type = <class 'int'> size = 28, object = 64
		 type = <class 'int'> size = 28, object = 13
		 type = <class 'int'> size = 28, object = 30
		 type = <class 'int'> size = 28, object = 90
		 type = <class 'int'> size = 28, object = 27
	 type = <class 'list'> size = 120, object = [67, 89, 55, 24, 65]
		 type = <class 'int'> size = 28, object = 67
		 type = <class 'int'> size = 28, object = 89
		 type = <class 'int'> size = 28, object = 55
		 type = <class 'int'> size = 28, object = 24
		 type = <class 'int'> size = 28, object = 65
	 type = <class 'list'> size = 120, object = [76, 39, 91, 38, 42]
		 type = <class 'int'> size = 28, object = 76
		 type = <class 'int'> size = 28, object = 39
		 type = <class 'int'> size = 28, object = 91
		 type = <class 'int'> size = 28, object = 38
		 type = <class 'int'> size = 28, object = 42
	 type = <class 'list'> size = 120, object = [41, 51, 59, 14, 86]
		 type = <class 'int'> size = 28, object = 41
		 type = <class 'int'> size = 28, object = 51
		 type = <class 'int'> size = 28, object = 59
		 type = <class 'int'> size = 28, object = 14
		 type = <class 'int'> size = 28, object = 86
'''

f = first_function(matrix)
'''
 type = <class 'list'> size = 120, object = [41, 13, 30, 10, 27]
	 type = <class 'int'> size = 28, object = 41
	 type = <class 'int'> size = 28, object = 13
	 type = <class 'int'> size = 28, object = 30
	 type = <class 'int'> size = 28, object = 10
	 type = <class 'int'> size = 28, object = 27
 type = <class 'int'> size = 28, object = 41
 
Итого size - 148
'''
s = second_function(matrix)
'''
 type = <class 'numpy.ndarray'> size = 320, object = [[41 13 30 10 27]
 [64 13 30 90 27]
 [67 89 55 24 65]
 [76 39 91 38 42]
 [41 51 59 14 86]]
 
	 type = <class 'numpy.ndarray'> size = 104, object = [41 13 30 10 27]
		 type = <class 'numpy.int64'> size = 32, object = 41
		 type = <class 'numpy.int64'> size = 32, object = 13
		 type = <class 'numpy.int64'> size = 32, object = 30
		 type = <class 'numpy.int64'> size = 32, object = 10
		 type = <class 'numpy.int64'> size = 32, object = 27
	 type = <class 'numpy.ndarray'> size = 104, object = [64 13 30 90 27]
		 type = <class 'numpy.int64'> size = 32, object = 64
		 type = <class 'numpy.int64'> size = 32, object = 13
		 type = <class 'numpy.int64'> size = 32, object = 30
		 type = <class 'numpy.int64'> size = 32, object = 90
		 type = <class 'numpy.int64'> size = 32, object = 27
	 type = <class 'numpy.ndarray'> size = 104, object = [67 89 55 24 65]
		 type = <class 'numpy.int64'> size = 32, object = 67
		 type = <class 'numpy.int64'> size = 32, object = 89
		 type = <class 'numpy.int64'> size = 32, object = 55
		 type = <class 'numpy.int64'> size = 32, object = 24
		 type = <class 'numpy.int64'> size = 32, object = 65
	 type = <class 'numpy.ndarray'> size = 104, object = [76 39 91 38 42]
		 type = <class 'numpy.int64'> size = 32, object = 76
		 type = <class 'numpy.int64'> size = 32, object = 39
		 type = <class 'numpy.int64'> size = 32, object = 91
		 type = <class 'numpy.int64'> size = 32, object = 38
		 type = <class 'numpy.int64'> size = 32, object = 42
	 type = <class 'numpy.ndarray'> size = 104, object = [41 51 59 14 86]
		 type = <class 'numpy.int64'> size = 32, object = 41
		 type = <class 'numpy.int64'> size = 32, object = 51
		 type = <class 'numpy.int64'> size = 32, object = 59
		 type = <class 'numpy.int64'> size = 32, object = 14
		 type = <class 'numpy.int64'> size = 32, object = 86

 type = <class 'numpy.int64'> size = 32, object = 41

Итого size 352
'''
t = third_function(matrix) # type = <class 'int'> size = 28, object = 41

# Результаты ДЗ №6
# Выводы:
# Итого реализованы три способа "Найти максимальный элемент среди минимальных элементов столбцов матрицы" и
# подсчитаны, сколько было выделено памяти под переменные.
# Первая функция - размер 148 + 148 (матрицы и size) = 296
# Вторая функция - размер 352 + 148 (матрицы и size) = 500 (Видимо numpy array весит много)
# Третья функция - размер 28 + 148 (матрицы и size) = 176
# Учитывая сложность фунцкии и памятозатратность  - лучше всего написана третья функция

# Результаты ДЗ №4
# print(first_function(matrix))
# print(second_function(matrix))
# print(third_function(matrix))

# для matrix (5,5)
# первый вариант - 1000 loops, best of 5: 1.89 usec per loop
# второй вариант - 1000 loops, best of 5: 5.62 usec per loop
# третий вариант - 1000 loops, best of 5: 1.93 usec per loop

# для матрица (10,10)
# первый вариант - 1000 loops, best of 5: 5.43 usec per loop
# второй вариант - 1000 loops, best of 5: 14 usec per loop
# третий вариант - 1000 loops, best of 5: 1.91 usec per loop

# для матрица (20,20)
# первый вариант - 1000 loops, best of 5: 17.7 usec per loop
# второй вариант - 1000 loops, best of 5: 38.9 usec per loop
# третий вариант - 1000 loops, best of 5: 1.99 usec per loop

cProfile.run('first_function(matrix)')
# 4 function calls in 0.000 seconds
cProfile.run('second_function(matrix)')
# 12 function calls in 0.000 seconds  - 5 раз вызывается функция min
cProfile.run('third_function(matrix)')
#  4 function calls in 0.000 seconds

# Вывод:
# Вторая функция содержит минимальное количество строк кода, однако не оптимально по времени
# Оптимальным агоритмом из всех трех перечисленных - третий 