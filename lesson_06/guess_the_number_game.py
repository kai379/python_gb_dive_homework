from random import randint


def guess_the_number(min_num=1, max_num=10, number_of_attempts=5):
    number = randint(min_num, max_num)
    user_number = -99999999
    attempt = 0
    print()
    print(f'Загадано число от {min_num} до {max_num}. Угадайте его ;)')
    print(f'У вас {number_of_attempts} попыток.')
    while user_number != number:
        if attempt == number_of_attempts:
            print('Не угадали =(')
            print(f'Попытки закончились.\nЗагаданное число {number}.')
            return False
        user_number = int(input('Введите число: '))
        if user_number > number:
            print('Не угадали =( Ваше число больше загаданного')
            print('----------')
            attempt += 1
        elif user_number < number:
            print('Не угадали =( Ваше число меньше загаданного')
            print('----------')
            attempt += 1
    print('Вы угадали число!!! =)')
    return True


if __name__ == '__main__':
    guess_the_number(1, 10, 3)
