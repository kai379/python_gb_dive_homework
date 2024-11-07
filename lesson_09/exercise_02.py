"""
Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.
"""

from random import randint

MIN_G_NUMBER = 1
MAX_G_NUMBER = 100
MIN_N_ATTEMPTS = 1
MAX_N_ATTEMPTS = 10


def game_validator(func):
    def inner(number: int, attempts: int):
        g_number = number if MIN_G_NUMBER <= number <= MAX_G_NUMBER else randint(MIN_G_NUMBER, MAX_G_NUMBER)
        n_attempts = attempts if MIN_N_ATTEMPTS <= attempts <= MAX_N_ATTEMPTS \
            else randint(MIN_N_ATTEMPTS, MAX_N_ATTEMPTS)
        return func(g_number, n_attempts)

    return inner


@game_validator
def guess_number(g_number: int, g_attempts: int):
    print(f'Введите число от {MIN_G_NUMBER} до {g_number}. У Вас {g_attempts} попыток.')
    unknown_number = randint(MIN_G_NUMBER, g_number)
    while g_attempts:
        user_number = int(input('Введите число: '))
        if user_number > unknown_number:
            print('Загаданное число меньше.')
        elif user_number < unknown_number:
            print('Загаданное число больше.')
        else:
            print('Вы угадали число!!!')
            return
        g_attempts -= 1
    print(f'Попытки закончились. Загаданное число {unknown_number}')


guess_number(120, 15)
