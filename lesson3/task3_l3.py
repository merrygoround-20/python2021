# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    num = [a, b, c]
    num.remove(min(a, b, c))
    return sum(num)


print(my_func(int(input('Введите a: ')), int(input('Введите b: ')), int(input('Введите c: '))))
