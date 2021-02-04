# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.

goods = []
while input('Хотите добавить товар? Введите да/нет: ') == 'да':
    number = int(input('Введите номер товара: '))
    info = {}
    info_key = input('Наименование: ')
    info_value = input('Цена товара: ')
    info_available = input('Кол-во товара: ')
    info[info_key] = (info_value, info_available)
    goods.append(tuple([number, info]))
print(goods)

analytics = {}
my_tuple = []
for good in goods:
    for info_key, info_value in good[1].items():
        if info_key in analytics:
            analytics[info_key].append(info_value)
        else:
            analytics[info_key] = [info_value]
print(analytics)
