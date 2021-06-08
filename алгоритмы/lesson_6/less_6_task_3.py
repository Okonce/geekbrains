'''
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не
меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
'''

import random

class StatisticsError(ValueError):
    ...

size = 9
array = [random.randint(0, 10) for _ in range(size)]
random.shuffle(array)
print(array)

'Воспользуюсь пирамидальной сортировкой'
'Также известна как сортировка кучей. ' \
'Этот популярный алгоритм, как и сортировки вставками или выборкой, сегментирует список на две части: ' \
'отсортированную и неотсортированную. Алгоритм преобразует второй сегмент списка в структуру данных «куча» (heap), ' \
'чтобы можно было эффективно определить самый большой элемент.'

'Алгоритм'
'Сначала преобразуем список в Max Heap — бинарное дерево, где самый большой элемент является вершиной дерева. ' \
'Затем помещаем этот элемент в конец списка. После перестраиваем Max Heap и снова помещаем новый наибольший элемент ' \
'уже перед последним элементом в списке. Этот процесс построения кучи повторяется, пока все вершины дерева не будут удалены.'

def heapify(array, heap_size, root_index):
    # Индекс наибольшего элемента считаем корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — допустимый индекс, а элемент больше,
    # чем текущий наибольший, обновляем наибольший элемент
    if left_child < heap_size and array[left_child] > array[largest]:
        largest = left_child

    # То же самое для правого потомка корня
    if right_child < heap_size and array[right_child] > array[largest]:
        largest = right_child

    # Если наибольший элемент больше не корневой, они меняются местами
    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(array, heap_size, largest)

def heap_sort(array):
    n = len(array)

    # Создаём Max Heap из списка
    # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении,
    # уменьшая счётчик i на 1
    for i in range(n, -1, -1):
        heapify(array, n, i)

    # Перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

def my_median(array):
    heap_sort(array)
    n = len(array)
    if n == 0:
        raise StatisticsError("no median for empty data")
    if n % 2 == 1:
        return array[n // 2]
    else:
        i = n // 2
        return (array[i - 1] + array[i]) / 2

median_value = my_median(array)
print(f'Медианное значение равно {median_value}')