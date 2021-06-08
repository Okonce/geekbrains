'''
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
'''

count = 0
matrix = []
s = []
while count < 4:
    row = input('Введите 4 элемента матрицы: ')
    row_new = [int(x) for x in row.split(' ')]
    matrix.append(row_new)
    s.append(sum(row_new))
    count += 1

matrix.append(s)

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
