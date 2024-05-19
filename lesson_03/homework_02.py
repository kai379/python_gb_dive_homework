# https://autotest.gb.ru/problems/94?lesson_id=433070
# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами.
# Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.

from collections import Counter

text = "Python 3.9 is the latest version of Python. It's awesome!"

text_list = text.lower().split()
for i in range(len(text_list)):
    if not 'A' <= text_list[i][-1] <= 'z':
        text_list[i] = text_list[i][:-1]

clear_list = []
for i in text_list:
    if '`' in i:
        clear_list.extend(i.split('`'))
    elif "'" in i:
        clear_list.extend(i.split("'"))
    else:
        clear_list.append(i)

text_list_del_num = [i for i in clear_list if i.isalpha()]

pre_res = list(Counter(text_list_del_num).items())
res_10 = pre_res[:10]
res_10 = sorted(res_10, key=lambda x: (-x[1], x[0]))
res_10 = sorted(res_10, key=lambda x: x[0], reverse=True)
res_10 = sorted(res_10, key=lambda x: -x[1])
print(res_10)
