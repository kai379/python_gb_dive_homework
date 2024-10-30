"""
Задача 3. Модуль для нахождения уникальных для обоих списков
элементов
Создайте модуль с функцией, которая принимает два списка и возвращает
список, содержащий только элементы, которые уникальны для обоих списков
"""


def unique_of_two(first_list, second_list) -> list:
    first_set, second_set = set(first_list), set(second_list)
    intersection_set = first_set.intersection(second_set)
    return list((first_set - intersection_set) | (second_set - intersection_set))


if __name__ == '__main__':
    print(unique_of_two([1, 2, 3], [2, 3, 4, 5]))

