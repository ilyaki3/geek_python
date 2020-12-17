"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
"""


def data(name, surname, years, city, e_mail, telephone):
    print('|'.join([name, surname, years, city, e_mail, telephone]))


name = input('Имя -> ')
surname = input('Фамилия -> ')
years = input('Возраст -> ')
city = input('Город -> ')
e_mail = input('e-mail -> ')
telephone = input('Номер телефона -> ')

data(name, surname, years, city, e_mail, telephone)
