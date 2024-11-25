"""
Задание №2.
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и значение по умолчанию.
При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""


def get_dict_value(some_dict, key, default):
    try:
        return some_dict[key]
    except KeyError:
        return default


dict_val = {'a': 78}
print(get_dict_value(dict_val, 'b', 123))
