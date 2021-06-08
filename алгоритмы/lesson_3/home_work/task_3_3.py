'''
4. Определить, какое число в массиве встречается чаще всего.
'''
import random
m = [random.randint(1, 10) for _ in range(100)]

max_element, count = 0, 0
for x in set(m):
    if m.count(x) > count:
        max_element = x
        count = m.count(x)