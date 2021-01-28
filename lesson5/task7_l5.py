# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

profit = {}
average = {}
prof = 0
average_profit = 0
i = 0
with open(r"C:\Users\1625201\Documents\GitHub\python2021\lesson5\text7.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        firm, form, revenue, costs = line.split()
        profit[firm] = int(revenue) - int(costs)
        if profit.setdefault(firm) >= 0:
            prof = prof + profit.setdefault(firm)
            i += 1
    if i != 0:
        average_profit = prof / i
        print(f'Прибыль средняя - {average_profit:.2f}')
    else:
        print(f'Прибыль у всех отсутсвует.')
    average = {'Средняя прибыль': round(average_profit)}
    profit.update(average)
    print(f'Прибыль каждой компании - {profit}')

json_content = [profit, average]
with open('text7.json', 'w') as f:
    json.dump(json_content, f, ensure_ascii=False)
    print(f'Создан файл: \n '
          f' {json_content}')
