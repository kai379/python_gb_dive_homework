"""
Задание 1. Модуль для подсчета количества повторений слов
Создайте модуль с функцией, которая получает список слов и возвращает
словарь, в котором ключи — это слова, а значения — количество их повторений
в списке.
"""


def counter(words: list) -> dict:
    counter_dict = {}
    for i in words:
        counter_dict.setdefault(i, 0)
        counter_dict[i] += 1
    return counter_dict


if __name__ == '__main__':
    words_list = ['aaa', 'bbb', 'aaa', 'bbb', 'ccc']
    print(counter(words_list))
