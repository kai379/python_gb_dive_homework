# https://autotest.gb.ru/problems/93?lesson_id=433070
# Дан список повторяющихся элементов lst.
# Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

lst = [1, 2, 3, 4, 5]
lst01 = []
for i in lst:
    if lst.count(i) > 1 and i not in lst01:
        lst01.append(i)
print(lst01)
