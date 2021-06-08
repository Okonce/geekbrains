import random

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)

# Сортирова пузырьком

# n = 1
# while n < len(array):
#     for i in range(len(array) - n):
#         if array[i] > array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]
#     n += 1
#     print(array)
#
# print(array)

# Сортировка выбором

def selection_sort(array):

    for i in range(len(array)):
        idx_min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        array[idx_min], array[i] = array[i], array[idx_min]

# selection_sort(array)
# print(array)

# Сортировка вставками

def insertion_soirt(array):
    for i in range(len(array)):
        spam = array[i]
        j = i

        while array[j-1] > spam and j > 0:
            array[j] = array[j-1]
            j -= 1
        array[j] = spam
        print(array)

# insertion_soirt(array)
# print(array)

# Алгоритм сортировки Шелла
def shell_sort(array):

    assert len(array) < 4000, 'Массив слишком большой. Используйте другую сортировку'

    def new_increment(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(array) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()

    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]

# shell_sort(array)
# print(array)

def quick_sort(array):

    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    s_ar, m_ar, l_ar = [], [], []

    for item in array:
        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)

        else:
            raise Exception('Случилось непредвиденное')

    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)

def quick_sort_no_memory(array, fst, lst):

    if fst >= lst:
        return

    print(array)
    pivot = array[random.randint(fst, lst)]
    i, j = fst. lst

    while i <= j:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    quick_sort_no_memory(array, fst, j)
    quick_sort_no_memory(array, i, lst)

# quick_sort_no_memory(array, 0, len(array) - 1)

def reverse(array):
    for i in range(len(array)//2):
        array[i], array[len(array) - i - 1] = array[len(array) - i - 1],  array[i]

# print('*' * 50)
# t = tuple(random.randint(0, 100) for _ in range(size))
# t = tuple(sorted(t))

from collections import namedtuple
from operator import attrgetter

class Person:
    ...

Person = namedtuple('Person', 'name, age')
p_1 = Person('Asd', 23)
p_2 = Person('sdfs', 45)
p_3 = Person('qr', 54)

people = [p_1, p_2, p_3]

def by_age(person):
    return person.age

result = sorted(people, key=by_age)
result_1 = sorted(people, key=attrgetter('age'))