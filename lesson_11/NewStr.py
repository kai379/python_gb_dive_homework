"""
Задание №1
Создайте класс Моя Строка, где: будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)
"""
import time


class NewStr(str):
    """Изменённый класс str с доп свойствами"""
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance


str_01 = NewStr('Записки диванного эксперта', 'Лолкекович')
print(str_01.author)
print(f'{str_01.time:.2f}')
print(str_01.split())
