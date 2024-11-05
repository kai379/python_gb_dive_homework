"""
Задание №2
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
# name  id  access_level
import json
import os


def enter_name():
    name = input('Введите имя: ')
    return name


def enter_id(set_id: set):
    while True:
        user_id = input('Введите id (число): ')
        if user_id.isdigit() and int(user_id) not in set_id:
            return int(user_id)
        elif not user_id.isdigit():
            print('Вы ввели не число. Повторите попытку.')
        else:
            print('Такой id есть в базе. Повторите попытку.')


def enter_access_level():
    while True:
        access_level = input('Введите уровень доступа (число от 1 до 7): ')
        if access_level.isdigit() and 1 <= int(access_level) <= 7:
            return access_level
        print('Уровень доступа введён не корректно. Повторите попытку.')


def add_prof_in_json(file_name):
    if not os.path.exists(file_name):
        file = open(file_name, 'w')
        file.close()
    user_name = enter_name()
    with open(file_name, 'r', encoding='utf-8') as file:
        dict_id = json.load(file)
        set_id = set()
        if dict_id:
            for value in dict_id.values():
                for key in value.keys():
                    set_id.add(int(key))
        # TODO Добавление при отсутствии ключей
        print(set_id)
        user_id = enter_id(set_id)
        user_lvl = enter_access_level()
        dict_id[user_lvl] = {user_id: user_name}
    with open(file_name, 'w') as file:
        json.dump(dict_id, file, indent=2, sort_keys=True)


if __name__ == '__main__':
    add_prof_in_json('user_file.json')
