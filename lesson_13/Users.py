"""
Задание №4.
Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
"""
import json


class Users:

    def __init__(self, name, user_id, user_lvl):
        self.name = name
        self.user_id = user_id
        self.user_lvl = user_lvl

    def __repr__(self):
        return f'({self.name}, {self.user_id}, {self.user_lvl})'


def load_users(path: str):
    result = set()
    with open(path, 'r', encoding='utf-8') as json_file:
        for user_level, value in json.load(json_file).items():
            for user_id, name in value.items():
                result.add(Users(name, user_id, user_level))
    return result


if __name__ == '__main__':
    a = load_users('user_file.json')
    print(a)
