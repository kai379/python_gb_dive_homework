# https://autotest.gb.ru/problems/97?lesson_id=433071
# Напишите функцию для транспонирования матрицы transposed_matrix,
# принимает в аргументы matrix, и возвращает транспонированную матрицу.

def transpose(matrix):
    matrix = list(list(i) for i in zip(*matrix))
    return matrix


print(transpose(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
