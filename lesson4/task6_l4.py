# Реализовать два небольших скрипта:

# print(list(range(3, 10 + 1, 1)))

from itertools import count, cycle

for i in count(3, 1):
    if i >= 10:
        break
    else:
        print(i)

# полностью повторяет весь список х раз (тут 6 раз)
count = 1
for i in cycle(['2, 4, 7, 9, 12']):
    if count > 6:
        break
    print(i)
    count += 1
