class Cell:
    '''
    Реализовать программу работы с органическими клетками.
    Необходимо создать класс Клетка.
    В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
    В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
    вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
    Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
    обычное (не целочисленное) деление клеток, соответственно.
    В методе деления должно осуществляться округление значения до целого числа.
    '''
    def __init__(self, number: int):
        self.number = number

    def __str__(self):
        return f'Количество клеток {self.number}'

    def __add__(self, other):
        '''
        Cложение. Объединение двух клеток.
        :param other:
        :return: При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
        '''
        return Cell(self.number + other.number)

    def __sub__(self, other):
        '''
        Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
        больше нуля, иначе выводить соответствующее сообщение.
        :param other:
        :return:
        '''
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            return 'Разница меньше нуля'

    def __mul__(self, other):
        '''
        Создается общая клетка из двух.
        :param other:
        :return: Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
        '''
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        '''
        Деление. Создается общая клетка из двух.
        Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
        :param other:
        :return:
        '''
        return Cell(int(self.number/other.number))

    def make_order(self, number_of_cell_in_row: int):
        a = ''
        x = number_of_cell_in_row // self.number
        if number_of_cell_in_row % self.number == 0:
            for n, _ in enumerate(range(x)):
                if n == x-1:
                    a += '*' * self.number
                else:
                    a += '*' * self.number + '\n'
        else:
            for n, _ in enumerate(range(x)):
                a += '*' * self.number + '\n'
            x = number_of_cell_in_row % self.number
            a += '*' * x
        return a
