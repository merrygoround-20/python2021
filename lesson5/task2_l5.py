# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open(r"C:\Users\1625201\Documents\GitHub\python2021\lesson5\text2.txt", encoding='utf-8') as f_obj:
    lines = f_obj.readlines()
    print(f'В файле строк: {len(lines)}')
    i = 1
    for string in lines:
        print(f'В строке {i} слов: {len(string.split())}')
        i += 1
