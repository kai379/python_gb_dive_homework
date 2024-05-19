# https://autotest.gb.ru/problems/95?lesson_id=433070
# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в
# качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Предметы не должны дублироваться.
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.

# Проверка тестом от GeekBrains
def test(items, max_weight, backpack):
    backpacks_test = []
    sorted_result = []
    for i in range(2**len(items)):
        backpack_test = {}
        weight = 0
        for j, item in enumerate(items):
            if i & (1 << j):
                if weight + items[item] <= max_weight:
                    backpack_test[item] = items[item]
                    weight += items[item]
                else:
                    break
        backpacks_test.append(backpack_test)

    full_result = [backpack_test for backpack_test in backpacks_test if backpack_test]
    result = []
    for item in full_result:
        if item not in result:
            result.append(item)

    x = 0
    for i in result:
        if dict(sorted(i.items(), key=lambda item: item[1], reverse=True)) == dict(sorted(backpack.items(), key=lambda item: item[1], reverse=True)):
            x += 1
    if x > 0:
        return print(True)
    else:
        return print(False)


# Мой код
def prog(items, max_weight):
    """ Не дорабатывал """
    # Делаю резервную копию items в save_items
    save_items = {}
    for i in items:
        save_items[i] = items[i]
    # Выполняю свой код
    backpack = {}
    while items and max_weight >= min(items[i] for i in items):
        for key in items:
            if key not in backpack and items[key] <= max_weight:
                backpack[key] = items[key]
                max_weight -= items[key]
                max_weight = round(max_weight, 2)
                del items[key]
                break
    # Возвращаю items в изначальное состояние из резервной копии для теста GeekBrains
    for i in save_items:
        items[i] = save_items[i]
    return backpack


# # 1
# items = {
#     "ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
# max_weight = 1.0
#
# backpack = prog(items, max_weight)
# test(items, max_weight, backpack)


# 2
# items = {
#     "ноутбук": 2.0,
#     "книги": 1.5,
#     "зарядное устройство": 0.5,
#     "бутерброды": 0.3,
#     "вода": 1.0
# }
# max_weight = 5.0
#
# backpack = prog(items, max_weight)
# max_weight = 5.0
#
# test(items, max_weight, backpack)

# # 3
# items = {
#     "лодка": 3.0,
#     "велосипед": 4.0,
#     "мангал": 2.0
# }
# max_weight = 2.0
#
# backpack = prog(items, max_weight)
#
# test(items, max_weight, backpack)
#
#
# # 4
# items = {
#     "спальник": 1.0,
#     "палатка": 2.0,
#     "термос": 0.5,
#     "карта": 0.1,
#     "фонарик": 0.2,
#     "котелок": 0.5,
#     "еда": 2.0,
#     "одежда": 1.0,
#     "обувь": 0.8,
#     "нож": 0.2
# }
# max_weight = 10.0
#
# backpack = prog(items, max_weight)
# test(items, max_weight, backpack)
