"""
Задание №4
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
"""
import csv
import json


def csv_to_json(file_name):
    dict_file = {}
    with open(file_name, 'r', newline='', encoding='UTF-8') as file:
        csv_reader = csv.reader(file)
        for i, value in enumerate(csv_reader):
            if i:
                value[1] = value[1].zfill(10)
                value[2] = value[2].capitalize()
                dict_file[hash(value[1] + value[2])] = (value[0], value[1], value[2])
    with open(file_name.rsplit('.')[0] + '_new_json.json', 'w') as file:
        json.dump(dict_file, file, indent=2)

# Вариант по приколу, формирование словаря в одну строку
# def csv_to_json(file_name):
#     dict_file = {}
#     with open(file_name, 'r', newline='', encoding='UTF-8') as file:
#         csv_reader = csv.reader(file)
#         dict_file = {hash(i[1].zfill(10) + i[2].lower()): (i[0], i[1].zfill(10), i[2].lower()) for num, i \
#                      in enumerate(csv_reader) if num != 0}
#     with open(file_name.rsplit('.')[0] + '_new_json.json', 'w') as file:
#         json.dump(dict_file, file, indent=2)


if __name__ == '__main__':
    csv_to_json('user_file.csv')
