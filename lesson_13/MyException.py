"""
Задание №3.
Создайте класс с базовым исключением и дочерние классы исключения:
○ ошибка уровня,
○ ошибка доступа.

Задание №6.
Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
Передавайте необходимые данные из основного кода проекта.
"""


class MyException(Exception):
    pass


class LevelError(MyException):
    def __init__(self, level):
        self.level = level

    def __str__(self):
        return (f'Ваш уровень доступа не позволяет создать такую учётную запись.\n'
                f'Введите уровень ниже {self.level}')


class AccessError(MyException):
    def __init__(self, user_id=None):
        if user_id is None:
            self.message = 'Вы не авторизованны. Доступ запрещён.'
        else:
            self.message = f'Вы ввели id = {user_id}. Такой id отсутствует в базе.'

    def __str__(self):
        return self.message
