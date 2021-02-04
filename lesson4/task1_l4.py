# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы

from sys import argv

script_name, hours, rate, bonus = argv, \
                                  input('выработка в часах: '), \
                                  input('ставка в час: '), \
                                  input('премия: ')

print(f'Зарпалата: {int(hours) * int(rate) + int(bonus)}')
