"""
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""
text = 'abrakadabra'
text_dict_iter = iter({ch: ord(ch) for ch in set(text)}.items())

for i in range(5):
    key, value = tuple(next(text_dict_iter))
    print(f'{key = } --> {value = }')
