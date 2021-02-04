# Программа запрашивает у пользователя строку чисел, разделенных пробелом.

def my_sum():
    res = 0
    while True:
        numbers = input('Введите числа через пробел. Для выхода введите q: ').split()
        for i in numbers:
            try:
                if i == 'q':
                    print(f'Суммма {res}. Конец программы')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Введите числа или q')
        print(f'Сумма {res}')


my_sum()
