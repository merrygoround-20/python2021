# Реализовать функцию, принимающую два числа (позиционные аргументы)

def num(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'Нельзя делить на ноль'
    except ValueError:
        return 'Введите цифры'


print(num(int(input('Введите x: ')), int(input('Введите y: '))))
