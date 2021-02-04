#  Представлен список чисел.

my_list = [2, 3, 1, 7, 5, 4, 10]
i = 0
new_list = []
for el in my_list:
    if el > my_list[i-1]:
        new_list.append(el)
    i += 1

print(new_list)
