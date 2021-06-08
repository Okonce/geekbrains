'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
 Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''

from collections import defaultdict
from collections import deque

def my_dex(string):
    dex = 0
    num = deque(string)
    num.reverse()
    for x, i in enumerate(num):
        dex += numbers_16[i] * 16 ** x
    return dex

def my_hex(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in numbers_16:
            if numbers_16[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)

numbers_10 = '0123456789ABCDEF'
numbers_16 = defaultdict(int)

for num, key in enumerate(numbers_10):
    numbers_16[key] = num

a = 'A2'
b = 'C4F'
a_dex = my_dex(a)
b_dex = my_dex(b)

print(f'Сумма чисел: {my_hex(a_dex + b_dex)}')
print(f'Произведение чисел: {my_hex(a_dex * b_dex)}')