'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]

# for line in matrix:
#     for item in line:
#         print(f'{item:>4}', end='')
#     print()

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

print(max_value)
