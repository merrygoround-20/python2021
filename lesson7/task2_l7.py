# Реализовать проект расчета суммарного расхода ткани на производство одежды.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Затраты ткани: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Абстрактно'


class Coat(Clothes):
    def consumption(self):
        return f'На пальто нужно: {self.param / 6.5 + 0.5 :.2f} м ткани'

    def abstract(self):
        return 'Абстрактно 2'


class Costume(Clothes):
    def consumption(self):
        return f'На костюм нужно: {2 * self.param + 0.3 :.2f} см ткани'

    def abstract(self):
        pass


coat = Coat(52)
costume = Costume(184)
print(coat.consumption())
print(costume.consumption())
print(coat.abstract())
