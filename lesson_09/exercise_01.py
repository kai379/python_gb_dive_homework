"""
Задание №1
Создайте функцию-замыкание, которая запрашивает два целых числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
"""
from random import randint

MIN_G_NUMBER = 1
MIN_N_ATTEMPTS = 1


def guess_number(number: int, attempts: int):
    g_number = randint(MIN_G_NUMBER, number)
    n_attempts = randint(MIN_N_ATTEMPTS, attempts)

    def inner():
        nonlocal n_attempts
        print(f'Введите число от {MIN_G_NUMBER} до {number}. У Вас {n_attempts} попыток.')
        while n_attempts:
            user_number = int(input('Введите число: '))
            if user_number > g_number:
                print('Загаданное число меньше.')
            elif user_number < g_number:
                print('Загаданное число больше.')
            else:
                print('Вы угадали число!!!')
                return
            n_attempts -= 1
        print(f'Попытки закончились. Загаданное число {g_number}')

    return inner



