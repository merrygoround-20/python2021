# Реализовать программу работы с органическими клетками, состоящими из ячеек.

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Размер клетки больше и равен: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Размер клетки меньше и равен: {sub} клеточкам' if sub > 0 else 'Клетки нет'

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(12)
cell_2 = Cell(2)
print(cell + cell_2)
print(f'\n{cell - cell_2}')
print(f'\nУмножение: {cell * cell_2}')
print(f'\nДеление: {cell / cell_2}')
print(f'\nОрганизация по рядам\n{cell.make_order(4)}')
