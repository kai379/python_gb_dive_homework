"""
Задача 2. Модуль для удаления дублирующихся подряд символов
Напишите модуль с функцией, которая принимает строку и возвращает строку с
удаленными дублирующимися подряд идущими символами. Например, строка
"aabbccaa" должна быть преобразована в "abca".

"""


def del_repeat(user_str):
    if not user_str:
        return user_str
    user_str_list = list(user_str[:1])
    for i in range(len(user_str)):
        if user_str_list[-1] != user_str[i]:
            user_str_list.append(user_str[i])
    return ''.join(user_str_list)


if __name__ == '__main__':
    print(del_repeat('aabbcfrr'))
