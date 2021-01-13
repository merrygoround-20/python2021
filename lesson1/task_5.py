# Запросите у пользователя значения выручки и издержек фирмы.

# выручка = revenue
# издержки = costs
# прибыль = profit
# убыток = loss
# рентабельность = profitability
# сотрудники = staff

revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

if revenue > costs:
    profit = revenue - costs
    print('Фирма отработала с прибылью! Прибыль равна:', profit)
    profitability = (profit / revenue) * 100
    print('Рентабельность фирмы равна:', '%.2f' % profitability, '%')
    staff = int(input('Сколько сотрудников в фирме: '))
    profit = (revenue - costs) / staff
    print('Прибыль на сотрудника равна:', '%.2f' % profit)

elif revenue < costs:
    loss = revenue - costs
    print('Фирма отработала в убыток:', loss)
