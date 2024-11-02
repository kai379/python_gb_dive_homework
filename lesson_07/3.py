"""
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
    - если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
    - если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало.
"""


def read_file(text_file):
    with open(text_file, 'r', encoding='utf-8') as file:
        return list(map(lambda x: x.strip(), file.readlines()))


def merger_files(new_file, numbers_file, names_file):
    numbers_file_list = read_file(numbers_file)
    names_file_list = read_file(names_file)
    print(len(numbers_file_list), len(names_file_list))

    with open(new_file, 'w', encoding='utf-8') as file:
        if len(numbers_file_list) >= len(names_file_list):
            for i in range(len(numbers_file_list)):
                num_res = float(numbers_file_list[i].split(' | ')[0]) * float(numbers_file_list[i].split(' | ')[1])
                if num_res > 0:
                    print(f'{names_file_list[i % len(names_file_list)].lower()} - {round(num_res)}', file=file)
                if num_res < 0:
                    print(f'{names_file_list[i % len(numbers_file_list)].upper()} - {abs(num_res)}', file=file)
        else:
            for i in range(len(names_file_list)):
                num_res_list = numbers_file_list[i % len(numbers_file_list)].split(' | ')
                num_res = float(num_res_list[0]) * float(num_res_list[1])
                if num_res > 0:
                    print(f'{names_file_list[i].lower()} - {round(num_res)}', file=file)
                if num_res < 0:
                    print(f'{names_file_list[i].upper()} - {abs(num_res)}', file=file)


if __name__ == '__main__':
    merger_files('merge_name_num.txt', 'random_int_float.txt', 'nickname.txt')
