# Задание №4
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

list_1 = [1, 2, 3, 4, 1, 2, 3, 4, 5]
counter = 0
i = 0
while len(set(list_1)) != len(list_1):
    if list_1.count(list_1[i]) == 2:
        list_1.remove(list_1[i])

print(list_1)

