"""
Задание №1
Вспоминаем задачу 3 из прошлого семинара.
Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json


def txt_to_json(file_name):
    with (
        open(file_name, 'r', encoding='utf-8') as file,
        open('new_json.json', 'w') as json_file
    ):
        txt_list = [line for line in file]
        # txt_dict = {key.capitalize(): value[:-1] for key, value in map(lambda x: x.split(' - '), txt_list)}
        txt_dict = {}
        for i in txt_list:
            key, value = i.split(' - ')
            txt_dict.setdefault(key.capitalize(), [])
            txt_dict[key.capitalize()].append(value[:-1])
        json.dump(txt_dict, json_file, indent=2)


txt_to_json('merge_name_num.txt')
