"""
Задание №1
✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""
import random as rnd


MIN_NUM = -1000
MAX_NUM = 1001


def add_rnd_num(file_name: str, quantity_lines: int):
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(quantity_lines):
            print(f'{rnd.randint(MIN_NUM, MAX_NUM)} | {rnd.uniform(MIN_NUM, MAX_NUM)}', file=file)


if __name__ == '__main__':
    add_rnd_num('random_int_float.txt', 10)

