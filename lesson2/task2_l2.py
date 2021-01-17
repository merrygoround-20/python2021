# Для списка реализовать обмен значений соседних элементов.

my_list = list(map(int, input('Введите числа : ').strip().split()))
print('Вы ввели числа:', my_list)

if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print('Числа после обмена : ', my_list)
