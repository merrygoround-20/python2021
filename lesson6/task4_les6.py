# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехали'

    def stop(self):
        return f'{self.name} остановка'

    def turn_right(self):
        return f'{self.name} поворот на право'

    def turn_left(self):
        return f'{self.name} поворот на лево'

    def show_speed(self):
        return f'Скорость {self.name} {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость town car {self.name} {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышает разрешенную для town car'
        else:
            return f'Скорость {self.name} разрешенная'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость work car {self.name} {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше разрешенной для work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} не полицейская машина'


sport = SportCar(90, 'красный', 'Феррари', False)
town = TownCar(55, 'черный', 'Киа', False)
work = WorkCar(65, 'желтый', 'Матис', True)
police = PoliceCar(120, 'синий',  'Форд', True)
print(work.turn_left())
print(f'Цвет {work.name} - {work.color}')
print(sport.show_speed())
print(town.show_speed())
print(police.police())
print(police.show_speed())
