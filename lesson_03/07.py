# Задание №7
# Погружение в Python | Коллекции
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

text = list(input())
res_for_el = {}
for i in text:
    if i != ' ' and i in res_for_el:  # ' ' просто так
        res_for_el[i] += 1
    else:
        if i != ' ':  # просто так
            res_for_el[i] = 1
print(res_for_el)

# for i in text:
#     res_for_el[i] = res_for_el.get(i, 0) + 1
# print(res_for_el)

# dict_keys = set(text)
# res_for_el = {}.fromkeys(dict_keys, 0)
# for i in text:
#     res_for_el[i] += 1
# print(res_for_el)
