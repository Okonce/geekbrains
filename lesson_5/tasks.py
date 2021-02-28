'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

# with open('tast1.txt', 'w') as file:
#     while True:
#         data = input()
#         if len(data) > 0:
#             file.write(data + '\n')
#         else:
#             break
'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

# l = ['name skjdlkjs slkjdld', 'sername', 'text jdjfk dkkdl dkdkld']
# with open('task2.txt', 'w') as file:
#     for x in l:
#         file.write(x + '\n')
#
# with open('task2.txt', 'r') as file:
#     lines = file.readlines()
#     print(f"Всего строк: {len(lines)}")
#     for num, line in enumerate(lines):
#         print(f"В {num+1} строке {len(line.split())} слов")

'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

# with open('/Users/assimarakhimbekova/PycharmProjects/geekbrains/lesson_5/task3.txt', 'r') as file:
#     lines = file.readlines()
#     sum_zp = 0
#     for line in lines:
#         data = line.split()
#         sum_zp += float(data[1])
#         if float(data[1]) < 20_000:
#             print(data[0])
#     print(f'средняя величина дохода сотрудников: {sum_zp/len(lines)}')

'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

# my_dict = {'One': 'Один', 'Two':'Два', 'Three': 'Три', 'Four': 'Четыре'}
# with open('task4.txt', 'r') as file, open('task4_new.txt', 'w') as file_new:
#     lines = file.readlines()
#     for line in lines:
#         data = line.split(' ')
#         print(data)
#         file_new.write(f'{my_dict[data[0]]} - {data[2]}')

'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

# with open('task5.txt', 'w') as file:
#     l = 0
#     while True:
#         data = input()
#         if len(data) > 0:
#             file.write(data + ' ')
#             l += float(data)
#         else:
#             print(f'Sum: {l}')
#             break

'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

# my_dict = {}
# with open('task6.txt', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         key = line.split(': ')
#         value = 0
#         for x in key[1].split(' '):
#             for y in x.split('('):
#                 try:
#                     value += float(y)
#                 except:
#                     pass
#         my_dict[key[0]] = value

'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json
with open('/Users/assimarakhimbekova/PycharmProjects/geekbrains/lesson_5/task7.txt', 'r') as file, open("my_file.json", "w") as write_f:
    lines = file.readlines()
    mean_pribyl, number, my_dict, average = 0, 0, {}, {}
    for num, line in enumerate(lines):
        data = line.split(' ')
        viruchka, izdershka = float(data[2]), float(data[3])
        pribil = viruchka - izdershka
        my_dict[data[0]] = pribil
        if  viruchka > izdershka:
            mean_pribyl += pribil
            number += 1
    average['average_profit'] = mean_pribyl/number
    json.dump([my_dict, average], write_f)