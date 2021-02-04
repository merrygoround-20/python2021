# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников

with open(r"C:\Users\1625201\Documents\GitHub\python2021\lesson5\staff.txt", encoding='utf-8') as f_obj:
    staff = {}
    for line in f_obj:
        key, value = line.split()
        staff[key] = value
        if int(value) < 20000:
            print(f'Зарплата меньше 20000: {key} - {value}')
