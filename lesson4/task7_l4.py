# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.

def fact():
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        yield temp


n = int(input('Введите число: '))
for el in fact():
    print(el)
