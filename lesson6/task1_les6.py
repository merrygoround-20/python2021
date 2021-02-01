# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running
# (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import time, ctime
from itertools import cycle


class TrafficLight:
    __color = 'красный'

    def running(self):
        colors = cycle(['красный', 'желтый', 'зеленый', 'желтый'])
        self.__color = next(colors)
        start_time = time()
        switch_time = time()
        print(f'Дата и время {ctime()}, Цвет: {self.__color}')
        while time() < start_time + 60:
            if (time() > switch_time + 7, time() > switch_time + 2)[self.__color == 'желтый']:
                switch_time = time()
                self.__color = next(colors)
                print(f'Дата и время {ctime()}, Цвет: {self.__color}')


my_light = TrafficLight()
my_light.running()
