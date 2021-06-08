# Алгоритм поиска всех простых числе до заданного N
n = int(input('До какого числа получить простые числа: '))

sieve = [x for x in range(n)]
sieve[1] = 0

for x in range(2, n):
    if sieve[x] != 0:
        j = x * 2
        while j < n:
            sieve[j] = 0
            j += x

results = [x for x in sieve if x != 0]