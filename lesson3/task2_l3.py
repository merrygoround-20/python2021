# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя

def data(name, surname, birth, city, email, phone):
    print(f'Данные: {name}, {surname}, {birth}, {city}, {email}, {phone}')


data(input('Ваше имя: '), input('Ваша фамилия: '), input('Ваша дата рождения: '), input('Ваш город: '),
     input('Ваш email: '), input('Ваш номер тел: '))
