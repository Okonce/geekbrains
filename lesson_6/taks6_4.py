class Car:

    '''
    4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
    (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
    повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
    Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
    (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
    Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
    Выполните вызов методов и также покажите результат.
    '''

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed > 0:
            print(f'{self.color} автомобиль {self.name} поехала')

    def stop(self):
        if self.speed == 0:
            print(f'{self.color} автомобиль {self.name} остановилась')

    def turn(self, direction):
        print(f'{self.color} автомобиль {self.name} повернала {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышена скорость {self.speed}! Сбавьте скорость!')

class SportCar(Car):
    def show_speed(self):
        if self.speed > 60 and self.is_police == False:
            print(f'{self.name} точно не полиция')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышена скорость {self.speed}! Сбавьте скорость!')


class PoliceCar(Car):

    def show_speed(self):
        if self.speed > 100:
            print(f'{self.color} Полиция-{self.name} гонится за кем-то, возможно!')


my_car = Car(40, 'white', 'ferrari')
print(my_car.name, my_car.color, my_car.speed, my_car.is_police)
my_car.go()
my_car.turn('left')
my_car.show_speed()

strange_car = TownCar(70, 'blue', 'mers')
strange_car.show_speed()

pol = PoliceCar(140, 'red', 'bag')
pol.go()
pol.show_speed()
