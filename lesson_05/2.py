"""
✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку
"""

text = 'abrakadabra'
text_dict = {ch: ord(ch) for ch in set(text)}
print(text_dict)