# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# тут вообще не понятно, честно говоря. Искала информацию про исключение того,
# что в скобках - ничего подходящего не нашла. Готовые решения тоже не работали. Вот это более менее.
# Ррезультат хотябы выдает в правильном виде. Я прям растроена.
# Где вообще искать расширенные варианты работы разных split и тд? Только основное пишут везде..

with open(r"C:\Users\1625201\Documents\GitHub\python2021\lesson5\text6.txt", encoding='utf-8') as f_obj:
    lessons = f_obj.readlines()
    less_count = dict()
    for less in lessons:
        less_count[less.split(':')[0]] = less.split(':')[1].strip()

    for les in less_count.keys():
        less_count[les] = sum([int(n) for n in less_count[les].split(' ') if n.strip().isdigit()])


if __name__ == '__main__':
    print(less_count)