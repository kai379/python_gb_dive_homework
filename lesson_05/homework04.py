"""
Задача 4. Генератор подстрок
Напишите генераторную функцию substrings(s), которая принимает строку s и возвращает генератор всех
возможных подстрок этой строки.
На вход подается строка abc
На выходе будут выведены обозначения:
"""


def substrings(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            yield s[i:j]


user_input = input('Введите строку: ')

for el in substrings(user_input):
    print(el)
