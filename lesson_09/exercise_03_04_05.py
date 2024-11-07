"""
Задание №3
Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
При повторном вызове файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции.
"""
import json
import os


def dec_repeater(count):
    results = []

    def inner(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return inner


def read_json(file_name: str) -> dict:
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='UTF-8') as file:
            return json.load(file)
    return {}


def write_json(file_name: str, dict_data: dict):
    with open(file_name, 'w') as file:
        json.dump(dict_data, file, indent=2)


def deco_func(func):
    def inner(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        res_dict = read_json(file_name)
        res_of_func = str(func(*args, **kwargs))
        res_dict[res_of_func] = {'args': [i for i in args]}
        res_dict[res_of_func].update(kwargs)
        write_json(file_name, res_dict)
        return res_of_func

    return inner


@dec_repeater(3)
def some_func(*args, **kwargs):
    results = 0

    for value in args:
        if isinstance(value, int | float) or isinstance(value, str) and value.isdigit():
            results += int(value)

    for key, value in kwargs.items():
        if isinstance(value, int | float) or isinstance(value, str) and value.isdigit():
            results += int(value)

    return results


some_func(7, 56, '10', 5.5, vol=13, age='34')

