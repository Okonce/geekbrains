# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = int(input())

max_number = 0
while n > 0:
    c = n % 10
    if c >= max_number:
        max_number = c
    n //= 10

print(max_number)