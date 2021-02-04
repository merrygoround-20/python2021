# Создать список и заполнить его элементами различных типов данных.
# Использовать функцию type() для проверки типа.

my_int = 17, 4, 2
my_float = 1.1, 2.2, 3.3
my_str = "Hello world"
my_list = ['hi', '111']
my_tuple = ('bye', '222')
my_dict = {'name': 'Ivan', 'surname': 'Ivanov'}
my_set = {'c', 'm', 'w'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict, my_set]

for i in super_list:
    print(f'{i} is {type(i)}')
