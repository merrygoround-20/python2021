# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую
# его же, но с прописной первой буквой.
# Например,

# просто
# text = input('Напишите слово: ')

# print(text.title())

# способ 2
def int_func(text):
    return text.title()


print(int_func(input('Введите слово: ')))

# способ 3

def my_func():
    first_letter_small = text[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + text[1:]


source = input('Введите слова через пробел: ').split()
result = []
for text in source:
    result.append(my_func())
print(' '.join(result))

# способ 4

def int_func():
    word = input("Введите слова через пробел: ")
    print(word.title())
    return


int_func()
