# Задание №1
# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

list_01 = [1, 2, 3, 3, 2, 5, 4, 4]
res = []
for i in list_01:
    if i not in res:
        res. append(i)
print(res)
