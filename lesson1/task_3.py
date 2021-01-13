# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = int(input('Введите число: '))

n = str(number)
number2 = n + n
number3 = n + n + n
result = number + int(number2) + int(number3)

print('Равно:', result)
