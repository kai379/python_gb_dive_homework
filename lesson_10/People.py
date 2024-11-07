"""
Задание №3
Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения возраста на год,
full_name для вывода полного ФИО и т.п. на ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст
"""


class People:

    def __init__(self, initials: str, age: int):
        self.initials = initials
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self) -> str:
        return self.initials


if __name__ == '__main__':
    people_1 = People('KAI', 18)
    print(people_1.initials)
    # print(people_1._People__age)
    people_1.birthday()
    # print(people_1._People__age)
