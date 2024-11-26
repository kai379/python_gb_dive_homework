"""
Задание №4.
Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.

Задание №5.
Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
загрузка данных (функция из задания 4) вход в систему - требует указать имя и id пользователя.
Для проверки наличия пользователя в !множестве используйте магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение доступа.
А если пользователь есть, получите его уровень из !множества пользователей (почему не словарь?).
Добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
"""
import json
import os
from MyException import AccessError, LevelError


class Users:

    def __init__(self, name, user_id, user_lvl):
        self.name = name
        self.user_id = user_id
        self.user_lvl = user_lvl

    def __repr__(self):
        return f'({self.name}, {self.user_id}, {self.user_lvl})'

    def __eq__(self, other):
        if isinstance(other, Users):
            return self.name == other.name and self.user_id == other.user_id
        raise ValueError

    def __hash__(self):
        return hash(self.name + self.user_id + self.user_lvl)


class Company:
    def __init__(self, name, user_db_path):
        self.name = name
        self.path = user_db_path
        self.authorization = None

    @property
    def users(self) -> set[Users]:
        result = set()
        with open(self.path, 'r', encoding='utf-8') as json_file:
            for user_level, value in json.load(json_file).items():
                for user_id, name in value.items():
                    result.add(Users(name, user_id, user_level))
        return result

    def login(self, user_name, user_id):
        login_user = Users(user_name, user_id, 0)
        for user in self.users:
            if user == login_user:
                self.authorization = user
                print(f'Привет {user.name}! Ваш уровень доступа {user.user_lvl}')
                return user.user_lvl
        raise AccessError(user_id)

    def logout(self):
        print(f'{self.authorization.name} вышел.')
        self.authorization = None

    def is_valid_user_id(self, user_id: str):
        for users in self.users:
            if users.user_id == user_id:
                return False
        return True

    def load_json(self):
        if os.path.exists(self.path):
            with open(self.path, 'r', encoding='UTF-8') as users_db_json:
                users_db_dict = json.load(users_db_json)
        return users_db_dict

    def write_json(self, users_dict):
        with open(self.path, 'w', encoding='UTF-8') as users_db_json:
            json.dump(users_dict, users_db_json, indent=4, ensure_ascii=False)
        return f'Запись успешно завершена'

    def add_user(self, user_name: str, user_id: str, user_lvl: str):
        if not self.authorization:
            raise AccessError
        if self.authorization.user_lvl <= user_lvl:
            raise LevelError(self.authorization.user_lvl)
        else:
            if self.is_valid_user_id(user_id):
                users_db_dict = self.load_json()
                users_db_dict[user_lvl].update({user_id: user_name})
                self.write_json(users_db_dict)
                print('Пользователь успешно добавлен.')
            else:
                print('Такой id уже занят.')


if __name__ == '__main__':
    company = Company('LolProduct', 'user_file.json')
    company.login('Petr', '42')
    # company.add_user('NewUser2', '42', '7')
