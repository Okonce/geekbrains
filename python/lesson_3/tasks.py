from string import ascii_lowercase, whitespace, punctuation

def first_task(var_1: (int, float), var_2: (int, float)) -> float:
    '''
    1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
    '''
    try:
        return round(var_1 / var_2, 4)
    except ZeroDivisionError:
        return 'На ноль делить нельзя'

a, b = int(input()), int(input())
print(first_task(a,b))

def second_task(name: str, sername: str, year: str, city: str, email: str, tel: str) -> str:
    '''
    2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
    год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
    Реализовать вывод данных о пользователе одной строкой.
    '''
    return f'Информация о пользователе: имя {name}, фамилия {sername}, год рождения {year}, ' \
           f'город проживания {city}, почта: {email}, номер телефона {tel}'

print(second_task(name='Assima', sername='R', year='24.05.91', city='Innopolis',
          email='asima.astana@outlook.com', tel='8-888-888-88-88'))

def third_task(var_1: (int, float), var_2: (int, float), var_3: (int, float)) -> (int, float):
    '''
    3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
    наибольших двух аргументов.
    '''
    l = [var_1, var_2, var_3]
    l.sort(reverse=True)
    return l[0] + l[1]

print(third_task[10, 1000, 23])

def my_func_1_version(x: (int, float), y: int) -> (int, float):
    '''
    4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
    возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
    При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
    Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
    Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
    '''
    if y > 0 or type(y) == float:
        raise ValueError('Второе число должно быть целое отрицательное')
    return x ** y

print(my_func_1_version(2, -2))

def my_func_2_version(x: (int, float), y: int) -> (int, float):
    '''
    4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
    возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
    При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
    Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
    Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
    '''
    if y > 0 or type(y) == float:
        raise ValueError('Второе число должно быть целое отрицательное')
    d = 1
    for i in range(abs(y)):
        d *= x
    return 1 / d

print(my_func_2_version(2, -2))

def fifth_task():
    '''
    5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
    При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
    разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
    подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
    Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
    '''
    summer = 0
    smth_punc = [_ for _ in punctuation]

    while True:
        numbers = input()

        p = list(set(numbers).intersection(smth_punc))
        if p:
            l = []
            for x in numbers.split(p[0]):
                for y in x.split():
                    if y:
                        l.append(int(y))
        else:
            l = list(map(int, numbers.split()))

        if p:
            summer += sum(l)
            break
        summer += sum(l)
        print(summer)
    return summer

print(fifth_task())

def int_func(words: str) -> str:
    '''
    6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
    прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
    Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
    Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
    но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
    '''
    # If anything other than lower ascii letter is present, then return
    # error, else return words.title()
    for letter in words:
        if letter not in ascii_lowercase and letter not in whitespace:
            raise ValueError('Not correct data')
    return words.title()

a = input()
print(int_func(a))

