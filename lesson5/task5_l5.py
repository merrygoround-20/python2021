# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# не очень поняла что конкретно и на какой экран выводить: и в текстовом файле все выводится и тут

with open(r"C:\Users\1625201\Documents\GitHub\python2021\lesson5\text5.txt", "w+", encoding='utf-8') as f_obj:
    number = (input("Введите числа через пробел: "))
    f_obj.write(f'Ваши числа : {number} \n')
    numbers = sum(map(int, number.split(' ')))
    f_obj.write(f'Сумма чисел : {numbers}')
    print('Сумма чисел:', numbers)
