'''
8. Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).
'''

a, b, c = int(input('Введите первое число : ')), int(input('Введите второе число : ')), int(input('Введите треть число : '))
if a > b:
    if a < c:
        print(f'Среднее из трех числе {a}')
else:
    if b > c:
        print(f'Среднее из трех числе {c}')
    else:
        print(f'Среднее из трех числе {b}')