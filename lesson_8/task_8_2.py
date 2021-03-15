'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
'''

class OwnZeroDivisionError(ZeroDivisionError):
    def __init__(self, strs):
        self.strs = strs

a = int(input('Введите число: '))
b = int(input('Введите число: '))

try:
    if b == 0:
        raise OwnZeroDivisionError('My own division by zero')
    else:
        print(a/b)
except ZeroDivisionError as e:
    print(e)