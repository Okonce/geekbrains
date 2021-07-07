from itertools import cycle
from time import sleep


class TrafficLight:

    '''
    1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
    Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
    зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
    третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
    порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

    Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
    и завершать скрипт.
    '''

    def running(self):
        time_of_trafficlight = {'red': 7, 'yellow': 2, 'green': 5}
        for n, light in enumerate(cycle(time_of_trafficlight.keys())):
            if n == 9:
                break
            print(f'{light} - {time_of_trafficlight[light]} sec')
            sleep(time_of_trafficlight[light])

if __name__ == '__main__':
    trafic = TrafficLight()
    trafic.running()
