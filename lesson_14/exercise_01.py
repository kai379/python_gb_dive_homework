"""
Задание №1.
Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.

Задание №2.
Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import string
import doctest

text_orig = 'my string'
text_reg = 'My String'
text_punc = 'my string!'
text_rus = 'my stringстрока'
text_all = 'My, Stringстрока!'


def func(text: str):
    # """
    # >>> func(text_orig) == text_orig
    # True
    # >>> func(text_reg) == text_orig
    # True
    # >>> func(text_punc) == text_orig
    # True
    # >>> func(text_rus) == text_orig
    # True
    # >>> func(text_all) == text_orig
    # True
    # """
    return ''.join(i for i in text if i in string.ascii_letters or i.isspace()).lower()


if __name__ == '__main__':
    doctest.testmod(verbose=True)