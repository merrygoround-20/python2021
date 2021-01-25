# Реализовать формирование списка, используя функцию range() и возможности генератора.

# взяла от 10 до 100, чтоб покороче число влезло. проверила вручную ответ при от 2 до 10
from functools import reduce
old_list = list(range(10, 100 + 1, 2))


def my_f(num1, num2):
    return num1 * num2


print(reduce(my_f, old_list))
