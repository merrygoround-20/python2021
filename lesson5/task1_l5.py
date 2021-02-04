# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

lines = (input("Первое: "), input("Второе: "), input("Третье: "))
with open(r"C:\Users\1625201\Documents\GitHub\python2021\lesson5\text.txt", "w+", encoding='utf-8') as f_obj:
    for line in lines:
        f_obj.write(line + "\n")
        print(f_obj)
