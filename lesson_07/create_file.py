"""
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""
from string import ascii_lowercase
from random import randint, choice, randbytes
import os

__all__ = ['create_file', 'check_dir']


def check_dir(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


def create_name(min_len=6, max_len=30):
    return ''.join([choice(ascii_lowercase) for _ in range(randint(min_len, max_len))])


def check_file(dir_path: str, file_name: str, extension: str):
    if os.path.exists(os.path.join(dir_path, file_name + '.' + extension)):
        if '_' in file_name:
            file_name_list = file_name.split('_')
            file_name = file_name_list[0] + str(int(file_name_list[1]) + 1)
        else:
            file_name += '_1'
        return file_name


def create_file(dir_path, extension: str, min_bytes=256, max_bytes=4096, quantity=42):
    for _ in range(quantity):
        name = f'{create_name()}.{extension}'
        check_file(dir_path, name, extension)
        full_path = os.path.join(dir_path, name)
        with open(full_path, 'wb') as file:
            file.write(randbytes(randint(min_bytes, max_bytes)))


if __name__ == '__main__':
    create_file('test_dir', 'lol')
