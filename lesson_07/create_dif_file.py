"""
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""

from create_file import create_file, check_dir


def create_dif_file(dir_path, **kwargs):
    check_dir(dir_path)
    for extension, amount in kwargs.items():
        create_file(dir_path, extension, quantity=amount)


if __name__ == '__main__':
    create_dif_file('new_test', mp3=3, mpgv=4, koki=2)
