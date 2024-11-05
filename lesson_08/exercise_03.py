"""
Задание №3
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
"""
import json
import csv


def json_to_csv(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        file_dict: dict = json.load(file)
    with open(file_name.rsplit('.')[0] + '.csv', 'w', newline='', encoding='utf-8') as file:
        file_list = []
        for lvl, value in file_dict.items():
            for user_id, user_name in value.items():
                file_list.append([lvl, user_id, user_name])
        print(file_list)
        csv_writer = csv.writer(file, dialect='excel')
        csv_writer.writerow(['access level', 'id', 'name'])
        csv_writer.writerows(file_list)


if __name__ == '__main__':
    json_to_csv('user_file.json')
