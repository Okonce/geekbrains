class Stationery:
    '''
    Реализовать класс Stationery (канцелярская принадлежность).
    Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
    Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
    переопределен метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
    Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
    '''
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return f'Рисуем ручкой'

class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки с помощьью {self.title}'

class Handle(Stationery):
    def draw(self):
        return f'Пишем ручкой'


my_pen = Pen('pen')
print(my_pen.draw())

my_pen = Pencil('pen')
print(my_pen.draw())

my_pen = Handle('pen')
print(my_pen.draw())