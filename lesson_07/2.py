"""
Задание №2
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
from random import randint, randrange


MIN_LEN = 4
MAX_LEN = 7
VOWELS = 'aeiouy'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'


def generate_name() -> str:
    text = ''
    name_len = randint(MIN_LEN, MAX_LEN)
    for i in range(name_len):
        if i == 0:
            text += CONSONANTS[randrange(len(CONSONANTS))].upper()
        elif i == (name_len - 1):
            text += 'x'  # Сделаем имена галлов из Астерикса
        elif i % 2:
            text += VOWELS[randrange(len(VOWELS))]
        else:
            text += CONSONANTS[randrange(len(CONSONANTS))]
    return text


def nickname(file_name, quantity):
    with open(file_name, 'w', encoding='utf-8') as file:
        for _ in range(quantity):
            file.write(f'{generate_name()}\n')


if __name__ == '__main__':
    # test
    nickname('nickname.txt', 10)
