"""
Задание №1.
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


def get_num():
    num = input('Введите число: ')
    while True:
        try:
            return int(num)
        except ValueError:
            try:
                return float(num)
            except ValueError:
                print('Вы ввели не число. Попробуйте ещё раз.')


print(get_num())
