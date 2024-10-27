# https://autotest.gb.ru/problems/98?lesson_id=433071
# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def key_params(**kwargs):
    dict_for_reverse = kwargs
    dict_final = {}
    for key, value in dict_for_reverse.items():
        if type(value) is float:
            dict_final[value] = key
        elif isinstance(value, int or str or bool or frozenset or complex or tuple or bytes):
            dict_final[value] = key
        elif value is None:
            dict_final[None] = key
        else:
            dict_final[str(value)] = key
    return dict_final


# На входе
params = key_params(a=1, b='hello', c=[1, 2, 3], d={}, e=None, f=3.14)
print(params)

# На выходе
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}

