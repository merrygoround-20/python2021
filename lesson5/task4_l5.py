# Создать (не программно) текстовый файл со следующим содержимым:
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus = []
with open(r"C:\Users\1625201\Documents\GitHub\python2021\lesson5\text4.txt", encoding='utf-8') as f_obj:
    for i in f_obj:
        i = i.split(' ', 1)
        rus.append(translate[i[0]] + '  ' + i[1])
    print(rus)
with open(r"C:\Users\1625201\Documents\GitHub\python2021\lesson5\text4_2.txt", "w", encoding='utf-8') as f_obj2:
    f_obj2.writelines(rus)
